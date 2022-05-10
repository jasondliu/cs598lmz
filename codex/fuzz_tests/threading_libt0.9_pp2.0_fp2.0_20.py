import threading
threading.stack_size(2**26)

'''require moduls and create app for Flask'''
import logging
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_script import Manager

app = Flask(__name__)


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    #initialize SQLAlchemy
    db.init_app(app)

    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)

    return app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://finalproject:finalproject@localhost/finalproject'
app.secret_key = 'super secret key'

db = SQLAlchemy(app)

@app.before_first_request
def initialize():
    db.create_all()

#initialize ML algo
from
