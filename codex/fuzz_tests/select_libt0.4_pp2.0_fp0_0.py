import select
import socket
import sys
import time

from . import utils


class Server(object):
    def __init__(self, host, port, handler, max_clients=5):
        self.host = host
        self.port = port
        self.handler = handler
        self.max_clients = max_clients
        self.buffer_size = 4096

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.server.listen(max_clients)
        self.server.setblocking(0)

        self.inputs = [self.server]
        self.outputs = []
        self.message_queues = {}

    def serve_forever(self):
        while True:
            readable, writable, exceptional = select.select(
                self.inputs, self.outputs, self.inputs)
