import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import json
import time
import datetime
import random
from bson.objectid import ObjectId
from flask import Flask, request, render_template, session, url_for, redirect, jsonify
from flask_oauthlib.client import OAuth
from flask_oauthlib.client import OAuthException

import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

#
# Globals
#

app = Flask(__name__)
app.config['GOOGLE_ID'] = os.environ['GOOGLE_ID']
app.config['GOOGLE_SECRET'] = os.environ['GOOGLE_SECRET']
app.debug = True
app.secret_key = os.environ['FLASK_SECRET_KEY']
oauth = OAuth(app)

google = oauth.remote_app(
    'google',
    consumer_
