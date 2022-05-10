import threading
threading.stack_size(67108864)

import thread

from app import app, db
from app.models import User, Post, Product
from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm, ProductForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from app.email import send_password_reset_email
from app.forms import ResetPasswordRequestForm, ResetPasswordForm
from app.translate import translate
from guess_language import guess_language

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        language = guess_language(form.post.data)
        if language == 'UNKNOWN
