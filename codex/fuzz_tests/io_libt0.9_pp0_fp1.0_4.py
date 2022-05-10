import io
import urllib.request
import urllib.error
import urllib.parse
import socket
import ssl
import base64
import hashlib
import io

try: import json
except ImportError: import simplejson as json

import types

__all__ = [
    'create_token',
    'Http',
    'HTTPError',
    'RancherError',
]

import logging
logger = logging.getLogger(__name__)

def create_token(accessKey,secretKey):
    mac = hmac.new(secretKey.encode('utf-8'), digestmod=hashlib.sha256)
    now = datetime.datetime.utcnow()
    mac.update('{0} {1}'.format(
        accessKey.encode('utf-8'),
        now.strftime('%Y%m%dT%H%M%SZ').encode('utf-8'),
    ).encode('utf-8'))

    digest = base64.b64encode(mac.digest()).strip('\
