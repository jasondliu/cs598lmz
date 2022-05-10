import socket
import sys
import time

from threading import Thread

class Client(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self.sock.settimeout(None)
        self.sock.setblocking(True)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.sock.setsockopt(socket.SOL_TCP, socket.TCP_KEEPIDLE, 1)
        self.sock.setsockopt(socket.SOL_TCP, socket.TCP_KEEPINTVL, 1)
        self.sock.setsockopt(socket.SOL
