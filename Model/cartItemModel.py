from app import app, db   #,ma
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship

class CartItem(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    cartID=db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)
    vehiculoID=db.Column(db.Integer, db.ForeignKey('vehiculo.id'), nullable=False)
    quantity=db.Column(db.Integer, nullable=False)

    def __init__(self, cartID, vehiculoID, quantity):
        self.cartID=cartID
        self.vehiculoID=vehiculoID
        self.quantity=quantity

with app.app_context():
    db.create_all()