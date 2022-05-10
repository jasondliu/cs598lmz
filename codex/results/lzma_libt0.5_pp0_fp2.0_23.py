import lzma
lzma.LZMA_PRESET_EXTREME

import os
import re
import sys
import json
import time
import random
import requests
import subprocess
import threading
import traceback
from collections import deque
from datetime import datetime
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

import pymongo

import requests_cache
requests_cache.install_cache('requests_cache')

import lzma
lzma.LZMA_PRESET_EXTREME

import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# from . import common

import common

class Crawler:
