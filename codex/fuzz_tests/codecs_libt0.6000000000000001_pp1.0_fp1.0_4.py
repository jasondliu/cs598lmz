import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# MySQL Connector
import mysql.connector as mysql

# Flask
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, json

# Flask-Mail
from flask_mail import Mail

# Flask-Sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# Flask-Migrate
from flask_migrate import Migrate

# Flask-WTF
from flask_wtf import FlaskForm

# Flask-WTF - Recaptcha
from flask_wtf.recaptcha import RecaptchaField

# Flask-Login
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin

# Flask-Bootstrap
from flask_bootstrap import Bootstrap

# Flask-Bcrypt
from flask_bcrypt import Bcrypt

# Flask-JWT-Extended
from flask_jwt_extended import (JWTManager, jwt_
