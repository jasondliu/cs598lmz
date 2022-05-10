import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import config

from flask import Flask, render_template, request, jsonify, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from flask_mail import Mail, Message

from werkzeug.security import generate_password_hash, check_password_hash

from forms import LoginForm, RegisterForm, CreatePostForm, SearchForm, AddCommentForm
from models import User, Post, Comment, Tag, Follow, Like, db
from utils import *


app = Flask(__name__)
app.config.from_object(config)

mail = Mail(app)

db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
