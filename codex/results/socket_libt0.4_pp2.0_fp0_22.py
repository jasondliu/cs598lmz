import socket
import sys

from . import common
from . import config
from . import log
from . import ssl
from . import util

__all__ = ['Server']

class Server(object):
    """
    A simple SSL-enabled HTTP/1.1 server.
    """

    def __init__(self, address, handler, ssl_context=None, log=log.logger):
        """
        Construct a new server.

        :Parameters:
            - `address`: A tuple of ``(host, port)`` to listen on.
            - `handler`: A `RequestHandler` subclass.
            - `ssl_context`: An optional `ssl.SSLContext` instance.
            - `log`: An optional `logging.Logger` instance.
        """
        self.address = address
        self.handler = handler
        self.ssl_context = ssl_context
        self.log = log

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_
