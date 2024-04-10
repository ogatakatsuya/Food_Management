import os

class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///fooddb.sqlite"
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')