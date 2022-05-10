import select
import socket
import sys
import threading
import time

from . import config
from . import log
from . import utils
from . import web

class Server:
    def __init__(self, host, port, handler):
        self.host = host
        self.port = port
        self.handler = handler

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.server.listen(5)

        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

    def run(self):
        while True:
            client, address = self.server.accept()
            self.handler(client, address)

