from flask import Flask
from flask_sqlalchemy import SQLAlchemy # Object Relational Mapper
from flask_cors import CORS # Cross Orgin Request

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Not tracking all the changes

db = SQLAlchemy(app)