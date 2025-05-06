from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, IntegerField, DateTimeField, SelectField
from wtforms.validators import DataRequired
from datetime import datetime

class ProductForm(FlaskForm):
    product_id = StringField('Product ID')  
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    price = FloatField('Price', validators=[DataRequired()])


class MovementForm(FlaskForm):
    movement_id = IntegerField('Movement ID', validators=[DataRequired()])
    from_location = SelectField('From Location', choices=[], coerce=str)
    to_location = SelectField('To Location', choices=[], coerce=str)
    product_id = StringField('Product ID', validators=[DataRequired()])
    qty = IntegerField('Quantity', validators=[DataRequired()])
    timestamp = DateTimeField('Timestamp', default=datetime.utcnow, validators=[DataRequired()])
