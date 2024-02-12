# config.py
import secrets

class Config:
    MONGO_URI = 'mongodb://localhost:27017/dreambiztechsoft'
    secret_key = secrets.token_urlsafe(16)
    SECRET_KEY = "231b6f4296e832e223866ce2b0e0f7e0eed116bc6271f7b1785782e60f000903"
    # print(secret_key)