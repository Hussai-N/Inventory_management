from flask import Flask, render_template, request, redirect, url_for
from models import db, Product, Location, ProductMovement
from forms import ProductForm, MovementForm
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')  

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/product/add', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        print("Form is valid")

        last_product = Product.query.order_by(Product.product_id.desc()).first()
        
        if last_product:
            last_number = int(last_product.product_id[3:])
            new_number = last_number + 1
        else:
            new_number = 1
        
        new_product_id = f"PRD{new_number:03d}"

        new_product = Product(
            product_id=new_product_id,
            name=form.name.data,
            description=form.description.data,
            price=form.price.data
        )
        
        try:
            db.session.add(new_product)
            db.session.commit()
            print("Product added successfully")
        except Exception as e:
            db.session.rollback() 
            print(f"Error adding product: {e}")

        return redirect(url_for('view_products'))
    else:
        print("Form validation failed")
        print(form.errors)  

    return render_template('product_form.html', form=form)


@app.route('/products')
def view_products():
    products = Product.query.all()
    return render_template('view_products.html', products=products)

@app.route('/movement/add', methods=['GET', 'POST'])
def add_movement():
    form = MovementForm()
    if form.validate_on_submit():
        movement = ProductMovement(
            movement_id=form.movement_id.data,
            timestamp=form.timestamp.data,
            from_location=form.from_location.data or None,
            to_location=form.to_location.data or None,
            product_id=form.product_id.data,
            qty=form.qty.data
        )
        db.session.add(movement)
        db.session.commit()
        return redirect(url_for('view_report'))
    return render_template('movement_form.html', form=form)

@app.route('/product/edit/<string:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
  
    product = Product.query.get_or_404(product_id)  
    form = ProductForm(obj=product)  
    if form.validate_on_submit():
        product.product_id = form.product_id.data  
        product.name = form.name.data
        product.description = form.description.data
        product.price = form.price.data
        db.session.commit()  
        return redirect(url_for('view_products')) 
    return render_template('product_form.html', form=form, edit=True)



@app.route('/report/balance')
def view_report():
    movements = db.session.query(
        Product.name.label('product'),
        Location.name.label('location'),
        db.func.sum(
            db.case(
                (ProductMovement.to_location_id != None, ProductMovement.qty),
                (ProductMovement.from_location_id != None, -ProductMovement.qty),
                else_=0
            )
        ).label('qty')
    ) \
    .join(Product, Product.product_id == ProductMovement.product_id) \
    .outerjoin(Location, Location.location_id == ProductMovement.to_location_id) \
    .group_by(Product.name, Location.name) \
    .all()

    return render_template('report.html', balances=movements)



if __name__ == '__main__':
    app.run(debug=True)
