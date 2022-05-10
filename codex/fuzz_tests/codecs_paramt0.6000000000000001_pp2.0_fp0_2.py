import codecs
codecs.register_error("strict", codecs.ignore_errors)

from flask import Flask, render_template, request, jsonify, redirect, url_for, send_from_directory, session, flash
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_babel import Babel, gettext as _
from flask_wtf.csrf import CSRFProtect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from forms import LoginForm, RegisterForm, ForgotForm, ResetForm, ChangePasswordForm
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from flask_user import UserManager
from flask_user.forms import RegisterForm
from flask_user.signals import user_registered
from flask_user.roles_required import roles_required
from flask_user.recoverable import recover_password
from flask_user.changeable import
