import lzma
lzma.LZMAError

import sys
import getopt
import logging
import os
import time
import json

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(filename)s: %(message)s")
log = logging.getLogger(__name__)

import requests
from requests.exceptions import ConnectionError

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

from requests_futures.sessions import FuturesSession

from collections import OrderedDict
from json.decoder import JSONDecodeError

from pprint import pprint


class ApiError(Exception):
    def __init__(self, message, status=None):
        self.message = message
        self.status = status


class GremlinAPI(object):
    api_url = 'https://api.gremlin.com'

    def __init__(self, team_id, api_key, api_url=None):
        self.team_id = team_id

