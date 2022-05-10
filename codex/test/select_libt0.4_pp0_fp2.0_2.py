import select
import socket
import sys
import threading
import time

# The default port to listen on.
DEFAULT_PORT = 9999


class Client(object):
    """A client that connects to a server."""

    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.sock.setblocking(0)
        self.inputs = [self.sock]
        self.outputs = []
        self.running = True

    def run(self):
        """Run the client.

        This method will block until the client is done.
        """
        while self.running:
            readable, writable, exceptional = select.select(self.inputs,
                                                            self.outputs,
                                                            self.inputs)
