import select
import socket
import sys
import threading
import time
import tty
import termios

from . import protocol
from . import exceptions

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        self.client.setblocking(0)
        self.__send(protocol.join_command())

    def __send(self, data):
        self.client.send(data)

    def __recv(self):
        data = self.client.recv(1024)
        return data

    def __read_keys(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios
