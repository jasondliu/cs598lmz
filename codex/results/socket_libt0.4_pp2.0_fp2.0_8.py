import socket
import sys
import time
import urllib
import urllib2
import urlparse

import requests

from . import exceptions
from . import utils

# Python 2.6 compat
try:
    import json
except ImportError:
    import simplejson as json


class Client(object):
    def __init__(self, server_url, username=None, password=None,
                 auth_token=None, timeout=None, debug=False,
                 verify_ssl=True, ca_certs=None,
                 disable_ssl_certificate_validation=False,
                 disable_ssl_certificate_validation_warning=False,
                 proxies=None):
        """
        Initialize a new client to connect to a server.

        :param server_url: The base URL of the server.
        :type server_url: str
        :param username: The username to use to authenticate to the server.
        :type username: str
        :param password: The password to use to authenticate to the server.
        :type password: str
        :param auth_token:
