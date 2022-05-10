from bz2 import BZ2Decompressor
BZ2Decompressor.flush = lambda self: None

import datetime
import gzip
import http
import http.cookiejar
import mimetypes
import os
import pprint
import re
import shutil
import socket
import sys

try:
    # Python 3
    from io import BytesIO, StringIO
    from urllib.request import (HTTPCookieProcessor, HTTPError,
            Request, HTTPDefaultErrorHandler, build_opener, HTTPRedirectHandler,
            HTTPErrorProcessor)
except ImportError:
    # Python 2
    from StringIO import StringIO
    from io import BytesIO
    from urllib2 import (HTTPCookieProcessor, HTTPError,
            Request, HTTPDefaultErrorHandler, build_opener, HTTPRedirectHandler,
            HTTPErrorProcessor)

import xml.dom.minidom
import xml.sax
import xml

from lib.pyblosxom import tools
from lib.pyblosxom import _helper

def _get_config_data(config):
    data
