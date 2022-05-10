import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[1;31m')).start()

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, Email, EqualTo

from flask_socketio import SocketIO, Namespace, join_room, leave_room, emit
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from datetime import datetime

import numpy as np
import json
from collections import OrderedDict

from flask_migrate import Migrate

from flask_cors import CORS, cross_origin

# from gevent import monkey
# monkey.patch_all()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
