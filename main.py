# import models 

# import app and db
from app import app, db
from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

# define global functions and variables here 

# add routes and handlers here
@app.route('/', methods=['GET', 'POST'])
def home():
    # user validation handled in login route
    # use database queries provided by SQLAlchemy
    # e.g., User.query.filter_by(field_name=value).first()
    
    # user login status handled by adding user email to session after log in
    # session['user'] = user.email; check login status with if not 'user' in
    # session 

if __name__ == "__main__":
    app.run()