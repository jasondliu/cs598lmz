import ctypes
ctypes.windll.user32.SetProcessDPIAware()
# !pip install flask==0.12.4
# !pip install Flask-Login==0.4.1
# !pip install flask-wtf
# !pip install flask-sqlalchemy
# !pip install ftfy
# !pip install googletrans
from googletrans import Translator, LANGCODES,LANGUAGES
import json
from flask import Flask
from flask import render_template, request
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired,Email,Length
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import redirect
from flask import url_for
from flask import flash
from flask_bcrypt import Bcrypt
from ftfy import fix_text
from ftfy import fix_encoding
from flask import send_from_directory
