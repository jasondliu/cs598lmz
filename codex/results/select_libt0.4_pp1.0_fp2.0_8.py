import selectors
import socket
import types

from . import __version__
from . import utils


class Client:
    def __init__(self, host, port, selector, debug=False):
        self.host = host
        self.port = port
        self.debug = debug
        self.selector = selector
        self.sock = None
        self.response = b""
        self.request = None
        self.responses = []

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(False)
        try:
            self.sock.connect((self.host, self.port))
        except BlockingIOError:
            pass

        self.selector.register(self.sock, selectors.EVENT_READ | selectors.EVENT_WRITE, data=self)

    def service_connection(self):
        request = None
        if self.request:
            request = self.request
            self.request = None
        self
