import threading
# Test threading daemonic
threading.Thread.daemon = True

import string
import random

# Import an existing database connection
import db
import elasticsearch
# Start an internal call to use db info
conn = db.conn
cur = conn.cursor()

# Also use the db connection to access elasticsearch
# To send queries with python as if you were using
# the elasticsearch API
es = db.es

# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify

# Import module models (i.e. User)
# from app.mod_tweet.models import Tweet

# Import module forms
# from app.mod_tweet.forms import LoginForm

# Define the blueprint: 'tweet', set its url prefix: app.url/tweets/
mod_tweet = Blueprint('tweet', __name__, url_prefix='/tweet')


# Set the route and accepted methods
@mod_tweet.route('/analyze', methods=['GET'])
def analyze():
    """Render template
