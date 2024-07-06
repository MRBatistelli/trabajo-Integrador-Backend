from app import app, db   #,ma
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship

class Cart(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    userID=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    createdAt=db.Column(db.DateTime, default=db.func.current_timestamp())

    # Definir la relación con CartItem
    items = db.relationship('CartItem', backref='cart', lazy=True)
    def __init__(self, userID):
        self.userID=userID

with app.app_context():
    db.create_all()