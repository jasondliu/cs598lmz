from bz2 import BZ2Decompressor
BZ2Decompressor.__module__ = 'bz2'

import lzma
import sqlite3
import sys
import requests
import shutil
import logging

from .util import deprecated, import_member

logger = logging.getLogger(__name__)


def generate_token(token):
    if not isinstance(token, (tuple, list)):
        raise ValueError('tuple or list of string pairs is required')
    return '&'.join(['%s=%s' % (key, value) for key, value in token])


def sort_tokens(tokens):
    return ''.join(sorted([token.split('=')[0] for token in tokens]))


def has_login_token(url):
    return urlparse(url).path == '/gs/login'


def get_clientconfig_value(key):
    try:
        with open(os.path.join(os.getcwd(), 'client_' + key + 'Config.json')) as f:
            data = json.load(f)
        return data
