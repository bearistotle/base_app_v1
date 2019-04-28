from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = # 'db_type + db_driver://db_username:db_password@host:db_name'
# displays SQL command in command line window
app.config['SQLALCHEMY_ECHO'] = True 
app.config['SECRET_KEY'] = os.urandom(12)

db = SQLAlchemy(app)