import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import subprocess
import json
from datetime import datetime
from time import sleep
from flask import Flask, request, render_template, url_for, redirect, make_response, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from flask_socketio import SocketIO, send, emit, join_room, leave_room

# App config.
DEBUG = True

# Create app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441
