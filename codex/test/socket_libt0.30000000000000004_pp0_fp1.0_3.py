import socket
import sys
import threading
import time

from . import config
from . import log
from . import util
from . import version

# -----------------------------------------------------------------------------

class Client:
    """
    A client that connects to a server and sends requests.
    """

    def __init__(self, host, port, verbose=False):
        """
        Initialize the client.
        """
        self.host = host
        self.port = port
        self.verbose = verbose
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.connect((host, port))
        self.socket.settimeout(config.SOCKET_TIMEOUT)
        self.lock = threading.Lock()

    def send(self, request):
        """
        Send a request to the server.
        """
