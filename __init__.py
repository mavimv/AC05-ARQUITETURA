from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import *
import psycopg2

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]= DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    dbname=database,
)