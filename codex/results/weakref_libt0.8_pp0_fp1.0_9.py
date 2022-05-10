import weakref
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import request, render_template, redirect, url_for, flash
from flask_babel import gettext
from flask_login import login_required, current_user
from flask_wtf import RecaptchaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from itsdangerous import BadData
from jinja2 import Markup
from werkzeug.exceptions import BadRequest
from werkzeug.utils import secure_filename
from wtforms import Form, TextAreaField, SelectField, PasswordField, validators, fields, widgets
from wtforms.fields.html5 import EmailField
from wtforms.widgets import Input
from wtforms.widgets.html5 import NumberInput

from app.email import send_email
from app.firebase_auth import create_firebase_user
from app.models import User, db
from app.utils import UserInfo, fcm_push_data, get_app_version
