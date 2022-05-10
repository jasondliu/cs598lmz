import select
import sys
import time
import traceback

from . import util
from . import config
from . import log
from . import protocol
from . import crypto
from . import __version__

# A singleton instance of the server class
_server = None


class Server(object):
    """
    The server object is the main entry point for the application.
    It is a singleton that is created when the application starts.

    The server will create and manage multiple client objects.
    """

    def __init__(self):
        self.config = config.Config()
        self.log = log.Log(self.config)
        self.log.info("Starting server version %s" % __version__)

        self.clients = {}
        self.max_clients = self.config.getint("server", "max_clients")

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
