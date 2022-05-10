import socket
import sys
import time

from . import constants
from . import exceptions
from . import utils


class Client(object):
    """A client for the OpenTSDB HTTP API.

    :param str host: The hostname of the OpenTSDB server.
    :param int port: The port of the OpenTSDB server.
    :param str version: The version of the OpenTSDB server.
    :param str api_key: The API key to use for authentication.
    :param int timeout: The timeout for requests.
    """

    def __init__(self, host='localhost', port=4242, version='2.1',
                 api_key=None, timeout=None):
        self.host = host
        self.port = port
        self.version = version
        self.api_key = api_key
        self.timeout = timeout

    def _request(self, method, path, params=None, data=None):
        """Make a request to the OpenTSDB server.

        :param str method: The HTTP method to use.
        :param str path: The path to
