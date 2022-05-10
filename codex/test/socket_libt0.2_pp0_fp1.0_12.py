import socket
import struct
import sys
import time
import threading
import traceback

from . import config
from . import log
from . import util
from . import version

#
# Constants
#

#
# Classes
#

class Client(object):
    """
    Client class.
    """

    def __init__(self, host, port, timeout=None):
        """
        Initialize a new client.

        @param host: Hostname or IP address of the server.
        @type host: str
        @param port: Port number of the server.
        @type port: int
        @param timeout: Timeout in seconds.
        @type timeout: int
        """
        self.host = host
        self.port = port
        self.timeout = timeout
        self.socket = None
        self.lock = threading.Lock()
        self.log = log.getLogger(self)

    def connect(self):
        """
        Connect to the server.
        """
        self.lock.acquire()
