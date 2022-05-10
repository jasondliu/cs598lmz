import codecs
codecs.register_error('strict', codecs.ignore_errors)

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import text
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField, DateField, IntegerField
from wtforms.validators import DataRequired, Optional
from wtforms.widgets import TextArea

from flask_bootstrap import Bootstrap

from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mys
