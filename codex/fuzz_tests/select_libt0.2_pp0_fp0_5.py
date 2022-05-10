import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import util

# -----------------------------------------------------------------------------
#
# SERVER CLASS
#
# -----------------------------------------------------------------------------

class Server(object):
    """
    The Server class is the main class of the server. It is responsible for
    listening for connections, accepting them, and spawning a new thread to
    handle each connection.
    """

    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

        self.sock = None
        self.threads = []

    def start(self):
        """
        Start the server.
        """

        # Create a socket to listen for connections.
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.config.host, self.config.port))

