import select
import socket

from . import config
from . import log
from . import utils


class Connection(object):
    def __init__(self, sock, addr, fd):
        self.sock = sock
        self.addr = addr
        self.fd = fd
        self.buffer = b''
        self.closed = False
        self.send_buffer = b''

    def close(self):
        if not self.closed:
            self.closed = True
            self.sock.close()

    def send(self, data):
        self.send_buffer += data

    def recv(self):
        self.buffer += self.sock.recv(8192)
        return self.buffer

    def readable(self):
        return not self.closed and self.buffer

    def sendable(self):
        return not self.closed and self.send_buffer

    def fileno(self):
        return self.fd


class Server(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_
