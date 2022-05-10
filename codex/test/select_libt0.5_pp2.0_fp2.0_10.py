import select
import socket
import sys
import signal
import errno

from contextlib import contextmanager

class Server(object):
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port

    @contextmanager
    def create_server(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.hostname, self.port))
        sock.listen(100)
        sock.setblocking(0)

