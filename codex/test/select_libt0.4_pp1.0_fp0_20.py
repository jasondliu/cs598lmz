import select
import socket
import sys
import time
import traceback
from threading import Thread

from . import common
from . import config
from . import constants
from . import log
from . import util
from . import zmq

logger = log.get_logger(__name__)


class Connection(object):
    def __init__(self, addr, timeout=None):
        self.addr = addr
        self.timeout = timeout

        self.sock = None
        self.closed = False

    def connect(self):
        if self.sock is not None:
            return

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(self.timeout)
        sock.connect(self.addr)
        self.sock = sock

    def send(self, data):
        if self.closed:
            raise RuntimeError('Connection closed')

        self.connect()
        self.sock.sendall(data)

    def recv(self, n):
        if self.closed:
            raise
