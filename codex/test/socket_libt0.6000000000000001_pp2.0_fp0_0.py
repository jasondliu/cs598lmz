import socket
import sys
import time

from . import settings


class Sock(socket.socket):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connect_timeout = settings.SOCK_CONNECT_TIMEOUT
        self.read_timeout = settings.SOCK_READ_TIMEOUT
        self.write_timeout = settings.SOCK_WRITE_TIMEOUT
        self.settimeout(self.connect_timeout)

    def set_read_timeout(self, timeout):
        self.read_timeout = timeout
        self.settimeout(timeout)

    def set_write_timeout(self, timeout):
        self.write_timeout = timeout
        self.settimeout(timeout)

    def set_connect_timeout(self, timeout):
        self.connect_timeout = timeout
        self.settimeout(timeout)

