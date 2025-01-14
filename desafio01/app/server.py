from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from pymongo import MongoClient
from bson import ObjectId
import os

mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(mongo_uri)

db = client['DBPython']
collection = db['user']

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
       users = list(collection.find())

       for user in users:
           user['_id'] = str(user['_id'])
         
       return jsonify(users)

    def post(self):
        name = request.json['name']
        email = request.json['email']  

        data = { "name": name, "email": email }
        user = collection.insert_one(data)

        return jsonify({"message": "Added user!", "id": str(user.inserted_id)})

api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run()