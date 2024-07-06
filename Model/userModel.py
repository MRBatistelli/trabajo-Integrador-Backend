from app import app, db   #,ma
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    lastname=db.Column(db.String(100))
    mail=db.Column(db.String(100))
    gender=db.Column(db.String(100))
    age=db.Column(db.Integer)
    typeUser=db.Column(db.String(100))
    password=db.Column(db.String(100))
    admin = db.Column(db.Boolean, default=False)
    
    def __init__(self,name,lastname,mail,gender,age,typeUser,password, admin):
        self.name=name
        self.lastname=lastname
        self.mail=mail
        self.gender=gender
        self.age=age
        self.typeUser=typeUser
        self.password=password
        self.admin=admin

with app.app_context():
    db.create_all()