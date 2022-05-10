import socket
import threading
import time
import sys
import os
import random

from . import common
from . import config

class Client(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((config.HOST, config.PORT))
        self.sock.settimeout(config.TIMEOUT)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        self.send_thread = threading.Thread(target=self.send_thread)
        self.send_thread.daemon = True
        self.send_thread.start()

        self.recv_thread = threading.Thread(target=self.recv_thread)
        self.recv_thread.daemon = True
        self.recv_thread.start()
