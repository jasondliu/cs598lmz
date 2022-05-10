import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask.ext.pymongo import PyMongo
from flask.ext.login import LoginManager, login_user, logout_user, login_required, current_user

from bson import json_util
from bson.objectid import ObjectId

from random import choice
import string
import markdown
import os
import urllib

from werkzeug import secure_filename

import sys, traceback

app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.secret_key = '5X5q5g5B5h5H5J5G5R5Q5L5
