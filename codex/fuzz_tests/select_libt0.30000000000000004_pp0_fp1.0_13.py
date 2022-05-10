import selectors
import socket
import sys
import time
import types

from . import config
from . import log
from . import util
from . import version


class _Client:
    def __init__(self, sock, addr):
        self.sock = sock
        self.addr = addr
        self.data = b''
        self.closed = False

    def close(self):
        self.closed = True
        self.sock.close()

    def send(self, data):
        self.sock.sendall(data)

    def recv(self, size):
        while len(self.data) < size:
            try:
                self.data += self.sock.recv(1024)
            except BlockingIOError:
                return False
        data = self.data[:size]
        self.data = self.data[size:]
        return data


class _Server:
    def __init__(self, sock, addr):
        self.sock = sock
        self.addr = addr
        self.data = b''
        self.closed
