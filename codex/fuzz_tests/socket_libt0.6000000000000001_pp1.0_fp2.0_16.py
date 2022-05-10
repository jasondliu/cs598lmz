import socket
import sys

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from redis import Redis

from . import config
from . import models

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

redis = Redis(host=config.REDIS_URL.split(":")[0], port=config.REDIS_URL.split(":")[1])


def create_app(config_name="development"):
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(config.config.get(config_name))

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register the blueprints
    from .api import api_blueprint

    app.register_blueprint(api_blueprint)

    if sys
