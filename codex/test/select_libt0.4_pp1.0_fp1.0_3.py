import select
import socket
import sys
import threading
import time
import traceback

from . import util
from . import log

class Client:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.socket = None
        self.connected = False
        self.connect()

    def __del__(self):
        self.disconnect()

    def connect(self):
        if self.connected:
            return
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.socket.setblocking(0)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.connected = True

    def disconnect(self):
        if not self.connected:
            return
        self.socket.close()
        self.connected = False

