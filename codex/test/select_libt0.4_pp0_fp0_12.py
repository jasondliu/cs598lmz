import select
import socket
import sys
import time
import threading
import traceback
import weakref

import utils

logger = logging.getLogger(__name__)

class Connection(object):
    """
    A connection to a remote host.
    """
    def __init__(self, host, port, timeout=10):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = None
        self.connected = False
        self.lock = threading.Lock()

    def connect(self):
        if self.connected:
            return
