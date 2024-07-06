from app import app, db   #,ma
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship

class Vehiculo(db.Model):   # la clase Producto hereda de db.Model de SQLAlquemy   
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    brand=db.Column(db.String(100))
    model=db.Column(db.String(100))
    year=db.Column(db.Integer)
    price=db.Column(db.Integer)
    stock=db.Column(db.Integer)
    image=db.Column(db.String(400))
    
    def __init__(self,brand,model,year,price,stock,image): #crea el  constructor de la clase
        self.brand=brand # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.model=model
        self.year=year
        self.price=price
        self.stock=stock
        self.image=image        

with app.app_context():
    db.create_all()