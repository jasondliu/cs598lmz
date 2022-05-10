import socket
import sys
import time

from . import exceptions
from . import utils
from . import __version__

try:
    import ssl
except ImportError:
    ssl = None


class Connection(object):
    """
    A connection to a Redis server.

    This class abstracts the socket connection and the Redis protocol
    negotiation. It can be used as a context manager.
    """
    def __init__(self, host='localhost', port=6379, db=0, password=None,
                 socket_timeout=None, encoding='utf-8', encoding_errors='strict',
                 decode_responses=False, retry_on_timeout=False,
                 ssl=False, ssl_keyfile=None, ssl_certfile=None,
                 ssl_cert_reqs=None, ssl_ca_certs=None, max_connections=None):
        """
        Create a connection to the Redis server

        :param host: hostname or IP address of the Redis server
        :type host: str
        :param port: port
