import socket
import sys
import time

from . import constants
from . import exceptions
from . import utils
from . import version

# Python 2 and 3: alternative 4
try:
    import http.client as httplib
except ImportError:
    import httplib

if sys.version_info >= (3, 0):
    from urllib.parse import urlparse
else:
    from urlparse import urlparse


class BaseClient(object):
    """
    Base client for all the clients.

    :param api_key: Your api key.
    :param api_secret: Your api secret.
    :param api_version: The version of the api to use.
    :param api_url: The url of the api to use.
    :param timeout: The timeout of the requests.
    """

    def __init__(self, api_key=None, api_secret=None, api_version=None,
                 api_url=None, timeout=None):
        self.api_key = api_key
        self.api_secret = api_secret
        self.api
