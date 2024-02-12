# app/models.py
from app import mongo

class User:
    def create_user(self, username, password):
        mongo.db.users.insert_one({'username': username, 'password': password})

    def find_user(self, username):
        return mongo.db.users.find_one({'username': username})