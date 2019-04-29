from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['DEBUG'] = True
# 'db_type+driver://db_username:db_password@host:port/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://base_app_v1:base_app_v1@31.220.61.62:8889/base_app_v1'
# displays SQL command in command line window
app.config['SQLALCHEMY_ECHO'] = True 
app.config['SECRET_KEY'] = os.urandom(12)

db = SQLAlchemy(app)