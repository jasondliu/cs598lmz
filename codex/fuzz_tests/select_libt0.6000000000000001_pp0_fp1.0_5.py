import select
import sys
import threading
import time
import zlib

from . import config
from . import protocol
from . import util

def _run(client):
    """A function for use with the `threading` module that runs the client."""
    client.run()

class Client:
    """
    A `Client` is a connection to a server. It handles all networking.
    """

    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.socket.setblocking(0)
        self.running = False
        self.data = bytes()
        self.on_message = None
        self.on_error = None

    def run(self):
        """
        Runs the client. This will block until the client is stopped.
        """
        self.running = True
        while self.running:
            try:
                ready = select.select([self.socket], [], [], .1)
                if
