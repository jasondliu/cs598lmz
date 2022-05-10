import socket

import requests
import socketio

from flask import Flask, render_template
from flask_socketio import SocketIO

from flask_mongoengine import MongoEngine

from flask import render_template
from flask_babel import gettext
#from config import Config
# Create the Flask application and the Flask-SocketIO server
app = Flask(__name__)
app.config.from_object(Config)
db = MongoEngine()
db.init_app(app)
socketio = SocketIO(app)

# Configure the Flask-Babel module and the Jinja2 template autoescaper
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'fr'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'Europe/Paris'
#app.config['BABEL_TRANSLATION_DIRECTORIES'] = "translations/system"
app.jinja_env.autoescape = False
app.jinja_env.add_extension('jinja2.ext.i18n')



#
