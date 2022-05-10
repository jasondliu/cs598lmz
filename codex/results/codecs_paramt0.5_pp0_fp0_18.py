import codecs
codecs.register_error('strict', codecs.ignore_errors)

import sys
import os
import re
import json
import time
import datetime
import functools
import subprocess
import shlex

from collections import defaultdict
from collections import namedtuple

import requests
import requests_cache

from bs4 import BeautifulSoup

import pytz

from flask import Flask
from flask import jsonify
from flask import request
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

# Caching
requests_cache.install_cache('http_cache', expire_after=60*60*24)

# Config

# Path to the directory containing the `public` directory
STATIC_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to the directory containing the `public` directory
PUBLIC_DIR = os.path.join(STATIC_DIR, 'public')

# Path to the directory containing the `public/data` directory
DATA_DIR
