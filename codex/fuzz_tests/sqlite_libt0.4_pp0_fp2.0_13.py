import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import random
import string
import re
from datetime import datetime
from datetime import timedelta

from flask import Flask, render_template, request, redirect, url_for, session, g, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask_mail import Mail, Message

from forms import LoginForm, RegisterForm, ChangePasswordForm, ForgotPasswordForm, ResetPasswordForm

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

mail = Mail(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,
