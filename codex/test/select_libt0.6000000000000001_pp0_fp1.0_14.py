import select
import socket
import sys
import time
import tty
import traceback

class ConnectionError(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message
    def __str__(self):
        return self.message


class WifiConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.socket.setblocking(False)

    def disconnect(self):
        self.socket.close()
        self.socket = None

    def is_connected(self):
        return self.socket is not None

    def is_data_available(self):
        return select.select([self.socket], [], [], 0) == ([self.socket], [], [])

