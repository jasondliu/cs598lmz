import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from sqlalchemy.orm import joinedload

from flask import (Flask, request, session, g, redirect, url_for, abort,
                   render_template, json, flash, jsonify, Response, current_app)

import requests
from urlparse import urlparse

from boto.utils import parse_ts
import datetime
import calendar

from flask_debugtoolbar import DebugToolbarExtension

import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='/tmp/flask.log',
    filemode='a'
)
#logger = logging.getLogger(__name__)

from util import *
from models import *
from db import *
from forms import *
from ajax import *
from auth import *
from admin import *

from flask_assets import Environment, Bundle

# local config
