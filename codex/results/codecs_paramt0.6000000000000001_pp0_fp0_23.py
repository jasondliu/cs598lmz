import codecs
codecs.register_error('strict', codecs.ignore_errors)
from py2neo import Graph, Node, Relationship, authenticate
from flask import Flask, render_template, request, redirect, Response, flash, session, url_for, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, RadioField, TextAreaField, IntegerField, SelectMultipleField, widgets, HiddenField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo, NumberRange
from flask_paginate import Pagination, get_page_parameter
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required, current_user, roles_required
from flask_security.utils import encrypt_password
from flask_mail import Mail, Message
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_uploads import UploadSet, IMAGES, configure_uploads, UploadNotAllowed, patch
