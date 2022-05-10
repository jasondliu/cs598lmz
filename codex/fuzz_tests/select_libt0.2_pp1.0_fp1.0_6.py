import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import util
from . import version

__all__ = ['Server']

class Server(object):
    """
    A simple HTTP server.

    This server is designed to be used in conjunction with the
    :class:`~.RequestHandler` class.

    :param host: The hostname to listen on.
    :param port: The port to listen on.
    :param handler: The request handler class to use.
    :param ssl_context: An SSL context to use for HTTPS.
    :param log: The log to use.
    :param request_timeout: The timeout for requests.
    :param max_connections: The maximum number of connections.
    :param max_requests: The maximum number of requests per connection.
    """
    def __init__(self, host='', port=80, handler=None, ssl_context=None,
                 log=None, request_timeout=None, max_connections=None,
                 max_requ
