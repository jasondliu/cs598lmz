import select
import socket
import sys
import time

from . import __version__
from . import config
from . import log
from . import utils

logger = log.get_logger(__name__)


class Server(object):
    """A simple TCP server."""

    def __init__(self, host, port, handler, backlog=5, timeout=None):
        self.host = host
        self.port = port
        self.handler = handler
        self.backlog = backlog
        self.timeout = timeout
        self.socket = None
        self.running = False

    def start(self):
        """Start the server."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(self.backlog)
        self.running = True
        logger.info('Server started on %
