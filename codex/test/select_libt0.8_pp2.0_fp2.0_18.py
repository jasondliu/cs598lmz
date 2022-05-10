import selectors
from datetime import datetime
import errno
import os
import json
import requests
import sys
from urllib.parse import urlparse
import asyncio
import logging
from urllib3 import ProxyManager, proxy_from_url
from typing import List, Tuple, Dict

DEBUG = os.getenv('DEBUG', 'False') == 'True'

sel = selectors.DefaultSelector()
logger = logging.getLogger('proxy-checker')
if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

BASE_URL = 'http://ip-api.com/json/'
TIMEOUT = 10
TESTS = [
    (
        'http://ip-api.com/json/',
        {'ip': 'myip'},
    ),
]
TESTS: List[Tuple[str, Dict[str, str]]]

class Proxies:
    FILE_PATH = '../proxies.txt'

