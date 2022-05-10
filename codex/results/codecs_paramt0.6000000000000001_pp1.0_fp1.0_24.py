import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Note: this is a workaround for a problem with the Python 2.4.1
# library.  See http://bugs.python.org/issue1043234 for details.
try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

import sys
import getopt
import os
import re
import urllib
import urlparse
import socket
import httplib
import time
import errno
import mimetypes
import gzip
import StringIO
import copy
import cgi
import getpass
import types
import traceback
import hashlib
import hmac
import base64
import logging
import logging.handlers

try:
    import ssl
except ImportError:
    ssl = None

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

import boto
from boto import handler
from boto.pyami.config import Config, BotoConfigLocations
from boto.pyami.cred
