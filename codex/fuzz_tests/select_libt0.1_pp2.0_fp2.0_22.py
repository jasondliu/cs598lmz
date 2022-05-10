import select
import socket
import sys
import time
import traceback

from . import config
from . import log
from . import util
from . import version

#------------------------------------------------------------------------------

class Server(object):
    """
    A server that listens for connections from clients.
    """

    def __init__(self, port, handler_class):
        """
        Initialize the server.

        @param port: The port to listen on.
        @param handler_class: The class to use for handling connections.
        """
        self.port = port
        self.handler_class = handler_class
        self.socket = None
        self.running = False
        self.handlers = []

    def start(self):
        """
        Start the server.
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(('', self.port))
        self.socket.listen
