import codecs
codecs.register_error('strict', codecs.ignore_errors)

import gzip
import io
import os
import re
import sys
import time
import urllib.request, urllib.parse, urllib.error
import zlib

from . import __version__
from . import compat
from . import error
from . import http
from . import util
from . import version

try:
    import ssl
    ssl_support = True
except ImportError:
    ssl_support = False

# This is the default user agent string used by urllib2.  It includes
# information on the Python version, urllib2 version, and platform.
# urllib2.py uses this variable to build a User-Agent header that is
# sent to the server.

# The format of this string may change at any time.  Do not parse it
# for information.

# The user agent string is created by urllib2.py.  If you want to set
# a custom user agent, you should create your own OpenerDirector with a
# custom addheaders attribute.  For example:
