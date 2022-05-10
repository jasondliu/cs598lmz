import selectors
import socket
import sys
import time

from . import util
from . import protocol

log = logging.getLogger(__name__)


class Client(object):
    def __init__(self, host='localhost', port=4711, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = None
        self.selector = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def _connect(self):
        if self.sock:
            return
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self.selector = selectors.DefaultSelector()
        self.selector.register(self.sock, selectors.EVENT_READ)
