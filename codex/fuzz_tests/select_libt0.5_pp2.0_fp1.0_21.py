import select
import sys
import time
import json
import urllib.request
import urllib.parse
import urllib.error

from . import util

# Set up logging
_logger = logging.getLogger(__name__)

# Set up basic constants
_DEFAULT_TIMEOUT = 60
_DEFAULT_RETRY = 3
_DEFAULT_PORT = 80
_DEFAULT_SSL_PORT = 443
_DEFAULT_METHOD = 'GET'
_DEFAULT_VERSION = '1.1'
_DEFAULT_USER_AGENT = 'python/{0} urllib3/{1}'.format(sys.version.split()[0],
                                                      urllib3.__version__)
_DEFAULT_CA_CERTS = certifi.where()

# Set up basic headers
_ACCEPT_ENCODING = 'gzip,deflate'
_CONTENT_TYPE = 'application/x-www-form-urlencoded'

# Set up basic status codes
_OK = 200
_CREATED = 201
_ACCEPTED =
