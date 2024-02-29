import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY = "flamita"
    SESSION_COOKIE_SECURE = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    # Creamos la base de datos en el gestor (mysql+pymysql://<USER>:<PASSWORD>@<IP>/<Database>)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://IDGS-801:Qwerty123456@127.0.0.1/bdidgs801'
    SQLALCHEMY_TRACK_MODIFICATIONS = False