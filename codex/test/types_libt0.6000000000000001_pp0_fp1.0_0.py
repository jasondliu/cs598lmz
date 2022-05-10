import types
types.ModuleType.__repr__ = lambda self: "<module '{}'>".format(self.__name__)

from flask import session, request, g, redirect, url_for, abort, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash

from . import app
from .database import db_session
from .models import User

@app.before_request
def before_request():
    g.user = None
    if 'id' in session:
        g.user = User.query.get(session['id'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user:
        return redirect(url_for('index'))
    error = None
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user is None:
            error = 'Invalid username'
