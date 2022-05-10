import select
import socket
import sys
import time

import numpy as np

from dvs.event import Event
from dvs.util import get_time

class UDPConnection:
    """
    Class to handle UDP communication
    """
    def __init__(self, ip='127.0.0.1', port=12000, buffer_size=1024,
                 timeout=0.1, verbose=False):
        """
        Initialize UDP connection
        """
        self.ip = ip
        self.port = port
        self.buffer_size = buffer_size
        self.timeout = timeout
        self.verbose = verbose

        self.socket = None
        self.connected = False
        self.connect()

    def connect(self):
        """
        Connect to UDP server
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(self.timeout)
        self.connected = True

    def disconnect(self):
        """
        Disconnect from UDP server
        """
