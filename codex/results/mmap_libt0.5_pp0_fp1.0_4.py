import mmap
from os import path

from flask import Flask, jsonify, request
from flask_cors import CORS

from . import config
from . import util
from . import log
from . import store

from . import api

from . import index
from . import search
from . import explore
from . import track
from . import playlist

from . import auth

from . import errors
from . import exceptions

from . import app_config

from .api import api_bp
from .auth import auth_bp

from . import db
from . import cache

from . import user

import time

app = Flask(__name__)

app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/auth')

CORS(app)

# TODO: Remove
# app.register_blueprint(routes.routes_bp, url_prefix='/')

# TODO: Remove
@app.route('/')
def index_route():
    return jsonify
