import codecs
codecs.register_error('strict', codecs.ignore_errors)

from functools import wraps

from flask import Flask, request, abort, jsonify, make_response, g
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

from werkzeug.contrib.fixers import ProxyFix
from werkzeug.exceptions import HTTPException

from raven.contrib.flask import Sentry

from config import config

from .utils import crossdomain, jsonp

from .models import User, Task, TaskStatus, TaskResult, TaskResultStatus

from .tasks import celery, send_email

from . import api

from . import views

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    CORS(app)
    sentry = Sentry(app
