import selectors
import socket
import types
import sys
import signal
import errno
import os
import time
import logging
import threading
import traceback
import datetime

import config

logger = logging.getLogger(__name__)

class Connection:
    def __init__(self, sock, addr):
        self.sock = sock
        self.addr = addr
        self.buffer = ''
        self.read_buffer = ''
        self.write_buffer = ''
        self.read_size = 0
        self.write_size = 0

    def close(self):
        self.sock.close()
        self.sock = None

class Server:
    def __init__(self, host, port, max_connections):
        self.host = host
        self.port = port
        self.max_connections = max_connections
        self.connections = {}
        self.selector = selectors.DefaultSelector()
