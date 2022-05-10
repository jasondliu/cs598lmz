import socket
import sys
import time

import numpy as np

from . import _util

class _Socket(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def close(self):
        self.sock.close()

    def send(self, data):
        self.sock.send(data)

    def recv(self, size):
        return self.sock.recv(size)

    def recv_all(self, size):
        data = b''
        while len(data) < size:
            data += self.recv(size - len(data))
        return data

    def recv_until(self, delim):
        data = b''
        while not data.endswith(delim):
            data += self
