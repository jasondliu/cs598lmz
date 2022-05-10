import mmap
import os
import sys

from datetime import datetime

from flask import Flask, request, render_template, g, abort, session, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, current_user, login_required
#from flask.ext.openid import OpenID
from flask.ext.babel import Babel

from config import config

login_manager = LoginManager()
#oid = OpenID()
babel = Babel()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config['SECRET_KEY'] = 'devkey'
    app.config['SESSION_PROTECTION'] = 'strong'

    config[config_name].init_app(app)

    login_manager.init_app(app)
    #oid.init_app(app)
    babel.init_app(app)

    from .main import main as main_blueprint
    app.register_
