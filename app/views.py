# app/views.py
from flask import jsonify, request
from app import app
from app.controllers import signup, login

app.add_url_rule('/signup', 'signup', signup, methods=['POST'])
app.add_url_rule('/login', 'login', login, methods=['POST'])
