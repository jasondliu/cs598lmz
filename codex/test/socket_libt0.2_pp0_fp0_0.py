import socket
import sys
import time

from . import common
from . import config

class Client(object):
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
        self.sock.sendall(data)

    def recv(self, size):
        return self.sock.recv(size)

    def send_command(self, command, data=None):
        if data is None:
            data = b''
        self.send(common.pack_command(command, data))

    def recv_command(self):
        return common.unpack_command(self.recv(common.COMMAND_SIZE))

