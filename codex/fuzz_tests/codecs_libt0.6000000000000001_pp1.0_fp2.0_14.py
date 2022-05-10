import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

import os

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify

from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

# create our little application :)
app = Flask(__name__)
manager = Manager(app)

# Load default config and override config from an environment variable
app.config.update(dict(
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, 'app.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

db = SQLAlchemy(app)
migrate = Migrate(app
