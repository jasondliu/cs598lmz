import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
from sqlite3 import dbapi2 as sqlite
#import sqlite
from flask import Flask, render_template, Blueprint
from .config import*


app = Flask(__name__)
app.config.from_object(PythonConfig)

app.config['SQLITE_DB_PATH'] = '/home/pi/server/tflask/tflask/tflask.db'
app.config['SECRET_KEY'] = 'don\'t tell anyone'

db_path = app.config['SQLITE_DB_PATH']
secret_key = app.config['SECRET_KEY']

# Flask Router Blueprints Registration
from .views import blueprint_www
from .views import blueprint_login
from .views import blueprint_profile
from .views import blueprint_meter
from .views import blueprint_admin
from .views import blueprint_ajax

app.register_blueprint(blueprint_www)
app.register_blueprint(blueprint_login)
app.register_blueprint(blueprint_profile)
app.register_blueprint(blueprint_meter)
app.register_
