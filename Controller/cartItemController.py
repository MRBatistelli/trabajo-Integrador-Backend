from flask import  jsonify,request  #,Flask# del modulo flask importar la clase Flask y los métodos jsonify,request

from app import app, db,ma
from Model.cartItemModel import *
from Model.vehiculoModel import *

# Schema
class CartItemSchema(ma.Schema):
    class Meta:
        fields=('id', 'cartID', 'vehiculoID', 'quantity')

cartItem_schema=CartItemSchema()
cartItems_schema=CartItemSchema(many=True)

#Enpoints CartItem

@app.route('/cartitems',methods=['GET'])
def get_CartItems():
    all_cartitems=CartItem.query.all() 
    result=cartItems_schema.dump(all_cartitems)  
    return jsonify(result)    


@app.route('/cartitems/<id>',methods=['GET'])
def get_cartItem(id):
    cartItem=CartItem.query.get(id)
    return cartItem_schema.jsonify(cartItem) 


@app.route('/cartitems/<id>',methods=['DELETE'])
def delete_cartItem(id):
    cartItem=CartItem.query.get(id)
    db.session.delete(cartItem)
    db.session.commit()                     
    return cartItem_schema.jsonify(cartItem) 


@app.route('/cartitems', methods=['POST'])
def create_cartItem():
    #cartID, vehiculoID, quantity
    cartID=request.json['cartID']
    vehiculoID=request.json['vehiculoID']
    quantity=request.json['quantity']
    
    new_cartItem=CartItem(cartID, vehiculoID, quantity)
    db.session.add(new_cartItem)
    db.session.commit() # confirma el alta ////
    return cartItem_schema.jsonify(new_cartItem)


@app.route('/cartitems/<id>', methods=['PUT'])
def update_cart_item(id):
    try:
        cart_item = CartItem.query.get(id)
        if not cart_item:
            return jsonify({'message': 'CartItem not found'}), 404

        vehiculo = Vehiculo.query.get(cart_item.vehiculoID)
        if not vehiculo:
            return jsonify({'message': 'Vehiculo not found'}), 404

        # Reducir el stock del vehículo en 1
        vehiculo.stock -= 1
        
        db.session.commit()

        return jsonify({'message': 'CartItem updated successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500