import socket
from flask import Flask
from  gevent.wsgi import WSGIServer

app = Flask(__name__)
app.config.from_object('config')

from flask.ext.script import Manager,Shell
from flask.ext.mail import Mail,Message
from flask.ext.sqlalchemy import SQLAlchemy


from flask.ext.migrate import Migrate,MigrateCommand

from flask.ext.login import LoginManager
from config import config
from flask.ext.pagedown import PageDown
from flask.ext.moment import Moment

from flask.ext.cache import Cache



from  flask.ext.script import Command



db=SQLAlchemy()
mail=Mail()
moment=Moment()

pagedown=PageDown()



from .main import main as main_blueprint
from .auth import auth as auth_blueprint
from .api import api as api_blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint, url_prefix = '/auth')
app.register_blue
