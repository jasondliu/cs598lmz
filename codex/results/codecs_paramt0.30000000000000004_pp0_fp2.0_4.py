import codecs
codecs.register_error('strict', codecs.ignore_errors)

from flask import Flask, request, redirect, url_for, render_template, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_mail import Mail, Message
from flask_babel import Babel, lazy_gettext
from flask_babelex import Babel
from flask_babelex import Domain
from flask_babelex import gettext, ngettext, lazy_gettext
from flask_babelex import refresh
from flask_babelex import Babel
from
