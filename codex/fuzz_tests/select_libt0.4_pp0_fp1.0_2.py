import selectors
import socket
import types

from . import constants, exceptions, protocol


class Client:
    def __init__(self, host, port, selector=None):
        self.host = host
        self.port = port
        self.selector = selector
        self.sock = None
        self.response = b""
        self.request = None
        self.connections = {}

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(False)
        try:
            self.sock.connect((self.host, self.port))
        except BlockingIOError:
            pass

        self.selector.register(
            fileobj=self.sock, events=selectors.EVENT_READ, data=self.read
        )

    def read(self, conn, mask):
        response = conn.recv(4096)  # Should be ready
        if response:
            self.response += response
            if self.response.endsw
