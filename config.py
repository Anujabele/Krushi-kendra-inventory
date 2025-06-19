import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '9c27affc57702d45913cd8f1532ba5e1'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///krushi.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
