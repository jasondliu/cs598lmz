import types
types.FunctionType = types.LambdaType

import sys

# Check if we're running on Python 3
PY3 = sys.version_info[0] == 3

if PY3:
    # Python 3 imports
    from io import BytesIO as StringIO
    from urllib.parse import urlparse, urlencode
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
else:
    # Python 2 imports
    from StringIO import StringIO
    from urlparse import urlparse
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError

import warnings
import re
import datetime
import time
import math
import os
import json
import gzip
import zipfile
import tempfile
import shutil
import atexit
import copy
import csv

# Third party imports
import requests

# Globals
_TMP_DIR = None

# Constants
_BASE_URL = 'http://api.tradingeconomics.com/'
_CALENDAR
