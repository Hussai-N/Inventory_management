from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'product'
    product_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True)  
    price = db.Column(db.Float, nullable=False) 

class Location(db.Model):
    __tablename__ = 'location'
    location_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.Text, nullable=True) 
class ProductMovement(db.Model):
    __tablename__ = 'product_movement'

    movement_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    from_location_id = db.Column(db.String, db.ForeignKey('location.location_id'), nullable=False)  
    to_location_id = db.Column(db.String, db.ForeignKey('location.location_id'), nullable=False)  
    product_id = db.Column(db.String, db.ForeignKey('product.product_id'), nullable=False)  
    qty = db.Column(db.Integer, nullable=False) 

    from_location = db.relationship('Location', foreign_keys=[from_location_id])
    to_location = db.relationship('Location', foreign_keys=[to_location_id])

