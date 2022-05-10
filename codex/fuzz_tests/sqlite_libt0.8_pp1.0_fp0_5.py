import ctypes
import ctypes.util
import threading
import sqlite3
import time
import pickle
import os
import sys
import re

from apscheduler.scheduler  import Scheduler
import apscheduler.events 
from apscheduler.jobstores.shelve_store import ShelveJobStore
from apscheduler.jobstores.memory import MemoryJobStore

from flask import *
from flask.ext.assets import Bundle, Environment

import pycurl
from StringIO import StringIO

from BeautifulSoup import BeautifulSoup

app = Flask(__name__)
app.debug = True

assets = Environment(app)
assets.url = app.static_url_path
assets.directory = app.static_folder

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_instructor/<instructorname>/")
def get_instructor(instructorname):
    logger.info("Get instructor: " + instructorname)
    return jsonify({
        'name': instructor_list[instructorname].
