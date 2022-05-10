import socket
import sys

from . import utils

# This is the default port for the server.
DEFAULT_PORT = 1234

# The default hostname for the server.
DEFAULT_HOST = 'localhost'


class Client(object):
    """
    This class represents a client for the server.
    """

    def __init__(self, host=DEFAULT_HOST, port=DEFAULT_PORT):
        """
        Initializes the client.
        :param host: The hostname of the server.
        :param port: The port of the server.
        """
        self.host = host
        self.port = port

    def send(self, message):
        """
        Sends a message to the server.
        :param message: The message to send.
        :return: The response from the server.
        """
        # Create a socket.
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server.
        sock.connect((self.host, self.port))

        # Send the
