from flask import  jsonify,request  #,Flask# del modulo flask importar la clase Flask y los métodos jsonify,request

from app import app, db,ma
from Model.vehiculoModel import *

# Schema
class VehiculoSchema(ma.Schema):
    class Meta:
        fields=('id','brand','model','year','price','stock','image')


vehiculo_schema=VehiculoSchema()  # El objeto vehiculo_schema es para traer un producto
vehiculos_schema=VehiculoSchema(many=True)  # El objeto vehiculos_schema es para traer multiples registros de producto

#Endpoints Vehiculos

@app.route('/vehiculos',methods=['GET'])
def get_Vehiculos():
    all_vehiculos=Vehiculo.query.all() # el metodo query.all() lo hereda de db.Model
    result=vehiculos_schema.dump(all_vehiculos)  #el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)     # retorna un JSON de todos los registros de la tabla


@app.route('/vehiculos/<id>',methods=['GET'])
def get_producto(id):
    vehiculo=Vehiculo.query.get(id)
    return vehiculo_schema.jsonify(vehiculo)   # retorna el JSON de un producto recibido como parametro


@app.route('/vehiculos/<id>',methods=['DELETE'])
def delete_producto(id):
    vehiculo=Vehiculo.query.get(id)
    db.session.delete(vehiculo)
    db.session.commit()                     # confirma el delete
    return vehiculo_schema.jsonify(vehiculo) # me devuelve un json con el registro eliminado


@app.route('/vehiculos', methods=['POST']) # crea ruta o endpoint
def create_vehiculo():
    #print(request.json)  # request.json contiene el json que envio el cliente
    brand=request.json['brand']
    model=request.json['model']
    year=request.json['year']
    price=request.json['price']
    stock=request.json['stock']
    image=request.json['image']
    new_vehiculo=Vehiculo(brand,model,year,price,stock,image)
    db.session.add(new_vehiculo)
    db.session.commit() # confirma el alta
    return vehiculo_schema.jsonify(new_vehiculo)


@app.route('/vehiculos/<id>' ,methods=['PUT'])
def update_producto(id):
    vehiculo=Vehiculo.query.get(id)
 
    vehiculo.brand=request.json['brand']
    vehiculo.model=request.json['model']
    vehiculo.year=request.json['year']
    vehiculo.price=request.json['price']
    vehiculo.stock=request.json['stock']
    vehiculo.image=request.json['image']


    db.session.commit()    # confirma el cambio
    return vehiculo_schema.jsonify(vehiculo)    # y retorna un json con el producto