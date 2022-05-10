import select
import socket
import sys
import time
import logging
import errno

from . import utils

logger = logging.getLogger(__name__)

class Client(object):
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.socket = None
        self.is_connected = False

    def connect(self):
        if self.is_connected:
            return
        logger.info("Connecting to %s:%d", self.host, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(self.timeout)
        self.socket.connect((self.host, self.port))
        self.is_connected = True

    def disconnect(self):
        if not self.is_connected:
            return
        logger.info("Disconnecting from %s:%d", self.host, self.port)
        self.socket.close
