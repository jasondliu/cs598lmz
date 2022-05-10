import select
import socket
import sys
import time

from netaddr import IPAddress, IPNetwork

from . import client
from . import server
from . import common

class TCPSocket:
    def __init__(self, address):
        self.address = address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(address)
        self.sock.setblocking(0)
        self.sock.listen(5)

    def fileno(self):
        return self.sock.fileno()

    def accept(self):
        return self.sock.accept()

    def close(self):
        return self.sock.close()

class UDPSocket:
    def __init__(self, address):
        self.address = address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_
