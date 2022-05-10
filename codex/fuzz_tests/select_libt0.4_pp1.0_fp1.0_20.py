import select
import socket
import sys
import time

from common import *

class Server:
    def __init__(self, port):
        self.port = port
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_socket.bind(('', port))
        self.listen_socket.listen(1)
        self.clients = []
        self.poller = select.poll()
        self.poller.register(self.listen_socket, select.POLLIN)

    def run(self):
        while True:
            for fd, event in self.poller.poll():
                if fd == self.listen_socket.fileno():
                    self.accept_connection()
                else:
                    self.handle_connection(fd, event)

    def accept_connection(self):
        client_socket, address = self.
