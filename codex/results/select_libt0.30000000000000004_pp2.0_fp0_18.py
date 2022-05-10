import select
import socket
import sys
import threading
import time

from . import config
from . import log
from . import network
from . import util
from . import version


class Server(object):
    def __init__(self, host, port, handler):
        self.host = host
        self.port = port
        self.handler = handler
        self.thread = None
        self.running = False

    def start(self):
        if self.thread is not None:
            return
        self.running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        if self.thread is None:
            return
        self.running = False
        self.thread.join()
        self.thread = None

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.
