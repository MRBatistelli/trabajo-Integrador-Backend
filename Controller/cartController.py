from flask import  jsonify,request  #,Flask# del modulo flask importar la clase Flask y los métodos jsonify,request

from app import app, db,ma
from Model.cartModel import *

# Schema
class CartSchema(ma.Schema):
    class Meta:
        fields=('id', 'userID', 'createdAt')

cart_schema=CartSchema()
carts_schema=CartSchema(many=True)


#Enpoints Cart

@app.route('/carts',methods=['GET'])
def get_Carts():
    all_carts=Cart.query.all() 
    result=carts_schema.dump(all_carts)  
    return jsonify(result)    


@app.route('/carts/<id>',methods=['GET'])
def get_cart(id):
    cart=Cart.query.get(id)
    return cart_schema.jsonify(cart) 


@app.route('/carts/<id>',methods=['DELETE'])
def delete_cart(id):
    cart=Cart.query.get(id)
    db.session.delete(cart)
    db.session.commit()                     
    return cart_schema.jsonify(cart) 


@app.route('/carts', methods=['POST'])
def create_cart():
    
    userID=request.json['userID']
    
    new_cart=Cart(userID)
    db.session.add(new_cart)
    db.session.commit() # confirma el alta
    return cart_schema.jsonify(new_cart)