import select
import socket
import sys
import time
import traceback
import urllib
import urlparse

import pycurl

from . import __version__
from . import log
from . import utils
from . import config
from . import exceptions

class CurlError(exceptions.Error):
    pass

class Curl(object):
    """
    A wrapper around pycurl that provides a higher-level interface.

    This class is not thread-safe.
    """

    def __init__(self, url, data=None, headers=None,
                 connect_timeout=None, timeout=None,
                 proxy=None, proxy_auth=None,
                 user_agent=None,
                 follow_redirects=True,
                 max_redirects=5,
                 ca_certs=None,
                 client_cert=None,
                 client_key=None,
                 validate_cert=True,
                 debug=False,
                 log_file=None,
                 log_level=log.INFO,
                 log_func=None,
                 log_prefix=None
