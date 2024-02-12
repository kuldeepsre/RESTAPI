# app/controllers.py
from flask import jsonify, request
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash

from app.utils.response import ApiResponse

user_model = User()

def signup():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if not username or not password:

        return jsonify(ApiResponse(400, False, 'Username and password are required').to_dict()), 400

    existing_user = user_model.find_user(username)
    if existing_user:

        return jsonify(ApiResponse(400, False, 'Username already exists').to_dict()), 400

    # hashed_password = generate_password_hash(password, method='sha256')
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    user_model.create_user(username, hashed_password)
    return jsonify(ApiResponse(200, False, 'User created successfully').to_dict()), 200







def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if not username or not password:

        return jsonify(ApiResponse(401, False, 'Username and password are required').to_dict()), 401

    user = user_model.find_user(username)

    if user and check_password_hash(user['password'], password):

        return jsonify(ApiResponse(200, False, 'Invalid username or password').to_dict()), 200
    else:
        return jsonify(ApiResponse(401, False, 'Invalid username or password').to_dict()), 401

