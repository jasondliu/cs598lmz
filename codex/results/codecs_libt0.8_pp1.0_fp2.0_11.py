import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import json
import unittest
from flask import Flask, render_template, redirect, flash, url_for, g
from flask_sqlalchemy import SQLAlchemy
import requests
import os
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_login import (LoginManager, current_user, current_app, login_user, logout_user, login_required, UserMixin, AnonymousUserMixin, confirm_login, fresh_login_required)
from flask_bcrypt import Bcrypt
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)

bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = 'topsecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql
