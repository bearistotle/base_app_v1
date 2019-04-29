from app import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# add classes for db tables here

# maybe add fields to track what apps the user has enabled?
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.Date())
    phone_number = db.Column(db.String(11), nullable=False)

    def __init__(self, email, password_hash, date_created, phone_number):
        self.email = email
        self.password_hash = password_hash
        self.date_created = date_created
        self.phone_number = phone_number

    def __repr__(self):
        return f'<User: {self.email}>'

