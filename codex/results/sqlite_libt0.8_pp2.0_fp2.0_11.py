import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import signal

import six
import pyDes

from pymongo import MongoClient
from flask import Flask, request, render_template, session, redirect
from werkzeug.utils import secure_filename

from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField, PasswordField
from wtforms.validators import InputRequired, DataRequired, NumberRange

import logging

class Config:
    SECRET_KEY = os.urandom(24)
    WTF_CSRF_SECRET_KEY = os.urandom(24)
    SESSION_TYPE = 'filesystem'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Strict'

app = Flask(__name__)
app.config.from_object(Config())

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')
