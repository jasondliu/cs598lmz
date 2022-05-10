import select
import socket
import logging
import sys
import json

from . import config
from . import utils
from . import protocol
from . import constants
from . import errors


LOGGER = logging.getLogger(__name__)


class Client(object):
    """
    A client that can connect to a server and send requests.
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """
        Connect the client to the server.
        """
        self.socket.connect((self.host, self.port))

    def send(self, message):
        """
        Send a message to the server.
        """
        self.socket.send(message)
        self.socket.shutdown(socket.SHUT_WR)

    def receive(self, bufsize=1024):
        """
        Receive a message from the server.
        """
        data = self.
