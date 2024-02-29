# Importamos SQLAlchemy desde flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import datetime

# Creamos una instancia de SQLAlchemy
db = SQLAlchemy()

# Creamos la tabla de Alumnos pasandole el modelo de la db
class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String(50))
    primerApellido = db.Column(db.String(50))
    segundoApellido = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
    