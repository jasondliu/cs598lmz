from bz2 import BZ2Decompressor
BZ2Decompressor.INCREMENT_BUFFER_SIZE = 128*1024
from logging import warning
from logging import info
from optparse import OptionParser
from pprint import pprint
from stderr_integration import LoggerWriter, add_builtin_handlers, remove_builtin_handlers
from sys import path
from sys import stderr
from time import time
from time import sleep
from urllib2 import URLError  # only as fall-back error we can catch/raise
import rawes
from urllib2 import HTTPError
from urllib2 import ProxyHandler
from urllib2 import HTTPBasicAuthHandler
from urllib2 import Request
from urllib2 import build_opener
from urlparse import urlparse
from webbrowser import open
from webapp.app import settings
from webapp.app.models import requests
from webapp.app.utils import unsanitized_http_basic_auth
from wsgi_intercept import interceptor
from wsgi_intercept.requests_intercept import install_opener
from wsgi_intercept.requests_intercept
