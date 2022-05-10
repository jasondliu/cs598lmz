import socket
import sys
import threading
import time
import traceback

from . import __version__
from . import config
from . import log
from . import util

logger = log.get_logger(__name__)


class Client(object):
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(self.timeout)
        self.sock.connect((self.host, self.port))

    def disconnect(self):
        self.sock.close()

    def send(self, data):
        if self.sock is None:
            self.connect()
        if isinstance(data, str):
            data = data.encode('utf-8')
        self.sock.sendall(data)

    def receive(self, size=
