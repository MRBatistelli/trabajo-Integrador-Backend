from flask import  jsonify,request  #,Flask# del modulo flask importar la clase Flask y los métodos jsonify,request

from app import app, db,ma
from Model.userModel import *

# Schema
class UserSchema(ma.Schema):
    class Meta:
        fields=('id','name','lastname','mail','gender','age','typeUser','password', 'admin')


user_schema=UserSchema()
users_schema=UserSchema(many=True)

#Enpoints User

@app.route('/users',methods=['GET'])
def get_Users():
    all_users=User.query.all() 
    result=users_schema.dump(all_users)  
    return jsonify(result)    


@app.route('/users/<id>',methods=['GET'])
def get_user(id):
    user=User.query.get(id)
    return user_schema.jsonify(user) 


@app.route('/users/<id>',methods=['DELETE'])
def delete_user(id):
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()                     
    return user_schema.jsonify(user) 


@app.route('/users', methods=['POST'])
def create_user():
    
    name=request.json['name']
    lastname=request.json['lastname']
    mail=request.json['mail']
    gender=request.json['gender']
    age=request.json['age']
    typeUser=request.json['typeUser']
    password=request.json['password']
    admin=request.json['admin']
    new_user=User(name,lastname,mail,gender,age,typeUser,password,admin)
    db.session.add(new_user)
    db.session.commit() # confirma el alta
    return user_schema.jsonify(new_user)


@app.route('/users/<id>' ,methods=['PUT'])
def update_user(id):
    user=User.query.get(id)
    
    user.name=request.json['name']
    user.lastname=request.json['lastname']
    user.mail=request.json['mail']
    user.gender=request.json['gender']
    user.age=request.json['age']
    user.typeUser=request.json['typeUser']
    user.password=request.json['password']
    user.admin=request.json['admin']


    db.session.commit()    # confirma el cambio
    return user_schema.jsonify(user)    # y retorna un json con el producto