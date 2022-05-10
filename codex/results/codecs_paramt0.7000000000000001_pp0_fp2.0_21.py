import codecs
codecs.register_error('strict', codecs.ignore_errors)
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen
from urllib.parse import urlparse, parse_qs
import json
from json import JSONDecodeError

from . import settings

from . import log
from . import db
from . import file
from . import utils

from .index import Index

import datetime

def parse_date(date_str):
    return datetime.datetime.strptime(date_str, '%d/%m/%Y')

def parse_path(path):
    # /api/<action>
    parts = path.split('/')
    if len(parts) < 3:
        return None, None
    if parts[1] != 'api':
        return None, None
    return parts[2], parts[3:]

def parse_body(body):
    try:
        return json.loads(body.decode('utf-8'))
    except JSONDecodeError:
        return {}

class Handler(
