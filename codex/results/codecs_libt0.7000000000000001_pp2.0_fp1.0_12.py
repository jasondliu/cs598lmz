import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

import sys
sys.path.insert(0, 'C:/Users/Mateusz/PycharmProjects/projekt_jezyki_programowania/python/mapa')

from flask import Flask, request, render_template, url_for, redirect
from flask_googlemaps import GoogleMaps, Map
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.sql import func
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_moment import Moment

