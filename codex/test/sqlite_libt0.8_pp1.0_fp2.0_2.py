import ctypes
import ctypes.util
import threading
import sqlite3
import time
import random

import requests
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms import StringField, ValidationError
from wtforms.validators import DataRequired
from flask_login import LoginManager, login_user, logout_user, \
    login_required, UserMixin, current_user, flash
from flask_restful import reqparse, abort, Api, Resource
from requests.exceptions import ConnectionError

import random

# Defining our Flask app
app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SECRET_KEY'] = 'thisissupposedtobesecret!'


# Initializing our API
api = Api(app)

# Initializing our DB
db = SQLAlchemy(app)

# Initializing our LoginManager
login_manager
