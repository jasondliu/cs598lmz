import socket
import sys
import time

from . import config
from . import log
from . import utils

logger = log.get_logger(__name__)


class Client(object):
    """
    A client for the statsd server.

    >>> from pystatsd.client import Client
    >>> client = Client()
    >>> client.gauge('foo', 42)
    >>> client.timing('bar', 500)
    >>> client.increment('baz')
    """

    def __init__(self, host=None, port=None, prefix=None, maxudpsize=None):
        """
        Create a new client.

        :param host: The host to connect to.
        :param port: The port to connect to.
        :param prefix: The prefix to use for all stats.
        :param maxudpsize: The maximum size of a UDP packet.
        """
        self.host = host or config.HOST
        self.port = port or config.PORT
        self.prefix = prefix or config.PREFIX
        self.maxudps
