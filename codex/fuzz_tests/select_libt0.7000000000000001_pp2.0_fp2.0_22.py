import select
from hashlib import sha256
from time import time

from polka.common import *

class PolkaClient(object):
    """
    A client for the Polka online storage service.
    """
    def __init__(self, username, password, host=DEFAULT_HOST, port=DEFAULT_PORT,
            home=DEFAULT_HOME):
        """
        Initializes a new PolkaClient.

        Arguments:
        - `username`: The username to connect with.
        - `password`: The password to connect with.
        - `host`: The host to connect to.
        - `port`: The port to connect to.
        - `home`: The directory to store files.
        """
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.home = home
        self.socket = None
        self.logged_in = False

    def _send(self, data):
        """
        Sends data to the server.

        Arguments:
        - `
