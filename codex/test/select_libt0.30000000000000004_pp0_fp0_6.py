import select
import socket
import sys
import time

from . import common
from . import config
from . import log
from . import util

class Client(object):
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect((self.host, self.port))
        self.sock.setblocking(0)

    def disconnect(self):
        self.sock.close()

    def send(self, data):
        self.sock.sendall(data)

    def recv(self, size):
        return self.sock.recv(size)

    def recv_all(self, size):
        data = b''
        while len(data) < size:
            data += self.recv(size - len(data))
        return data
