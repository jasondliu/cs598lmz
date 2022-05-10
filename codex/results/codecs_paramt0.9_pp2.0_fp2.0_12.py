import codecs
codecs.register_error('utf-8-escape', codecs.lookup_error('surrogateescape'))
from . import querylib
from .querylib import Filter
from . import config
from . import sessionmanager
from . import authorization
from . import utils
from .querylib import QueryInfo
from .http import HTTPError
from .querylib import ServerError
from flask import request, Flask, Response
from functools import wraps
from dateutil import parser as dateparser
import codecs
import json
import time
import sys
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # set a secret key for sessions


def authorized(func):
    """check for authority to access resources
    """
    @wraps(func)
    def decorated_view(*args, **kwargs):
        try:
            if 'api_key' in request.args:
                user_api_key = request.args['api_key']
            else:
                user_api_key = request.cookies.get('api_key')
            output = authorization.verify
