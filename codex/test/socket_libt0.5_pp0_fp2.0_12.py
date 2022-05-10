import socket
import sys

from . import common
from . import log


class Proxy(object):
    """
    This class holds the proxy settings for a single proxy server.
    """

    def __init__(self, host, port, username=None, password=None,
                 rdns=False, bind_address=None, timeout=None):
        """
        Initialize a new Proxy object.

        Arguments:
            host (str): The proxy server hostname.
            port (int): The proxy server port.
            username (str): The username to authenticate with.
            password (str): The password to authenticate with.
            rdns (bool): Whether or not to do a reverse lookup on the
                connecting IP.
            bind_address (str): The local IP address to bind to.
            timeout (int): The timeout for the proxy connection.
        """

        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.rdns = rdns
        self.bind_address = bind_address
        self.timeout
