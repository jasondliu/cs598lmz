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

