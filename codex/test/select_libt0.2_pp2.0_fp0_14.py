import select
import socket
import sys
import threading
import time
import traceback

import pytest

from . import util

# This is a port that is unlikely to be in use.
PORT = 50000


class TestServer(object):
    def __init__(self, port):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('127.0.0.1', port))
        self.sock.listen(1)
        self.thread = threading.Thread(target=self.run)
