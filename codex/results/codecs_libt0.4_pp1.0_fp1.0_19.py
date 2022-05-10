import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import logging
import logging.handlers
import time
import datetime
import json
import requests
import re
import urllib
import urllib2
import random
import string
import sqlite3
import threading
import Queue
import traceback
import base64
import hashlib
import hmac
import time
import math
import copy
from collections import deque
from datetime import datetime
from datetime import timedelta
from urllib2 import URLError, HTTPError
from requests.exceptions import ConnectionError
from requests.exceptions import Timeout
from requests.exceptions import HTTPError
from requests.exceptions import TooManyRedirects
from requests.exceptions import RequestException
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.packages.urllib3.exceptions import InsecurePlatformWarning
from requests.packages.urllib3.exceptions import SNIMissingWarning
from requests.
