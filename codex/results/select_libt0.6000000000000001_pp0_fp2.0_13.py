import select
import socket
import sys
import time
import threading

from . import packet
from . import utils
from . import config
from . import log

class Server(object):
    """
    Server class.

    The server listens for incoming connections on the port specified in the
    configuration file.
    """

    def __init__(self, config_file, log_file):
        """
        Constructor.
        """

        # Read configuration file.
        self.config = config.Config(config_file)

        # Initialize logger.
        self.log = log.Log(log_file)

        # Initialize server socket.
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Initialize list of clients.
        self.clients = []

        # Initialize list of ip addresses of clients.
        self.client_ips = []

        # Initialize list of client
