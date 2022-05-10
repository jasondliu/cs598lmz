import threading
# Test threading daemon
import time
import json
import requests

# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import db, login_manager

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app.mod_auth.models import User, OAuth

# Import module models (i.e. User)
from app.mod_auth.models import User

# Import module forms
from app.mod_auth.forms import LoginForm, RegisterForm, OAuthForm

# Import module views
#from app.mod_auth.views import mod_auth

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods
@mod_auth.route('/sign
