import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf-8' else None)

import os

from flask import (Flask, Blueprint, render_template, request, session, redirect, Markup, 
	send_from_directory, url_for, current_app, jsonify, flash)
from flask.ext.mako import render_template, MakoTemplates
from flask.ext.sslify import SSLify
import flask.ext.login as flask_login

from models import *
from utils import *
from forms import *

from urllib2 import urlopen, Request
import json

import requests

from functools import wraps

# Set up Flask app
app = Flask(__name__, template_folder="templates")
sslify = SSLify(app)
mako = MakoTemplates(app)

app.secret_key = os.urandom(24)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# Set up Blueprints
admin_blueprint = Blueprint('
