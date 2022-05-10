import socket
import math
import time
import json
import sys
import datetime as dt

from lib import configuration
from lib.utils import log, log_socket

config = configuration.load_configuration()

SOCKET_BUFFER_SIZE = 4096

class UDPListener(object):
    def __init__(self, host, port, callback, max_queue_length=10):
        self.host = host
        self.port = port
        self.callback = callback
        self.max_queue_length = max_queue_length

        self.s = None
        self.thread = None
        self.stop = threading.Event()

        # Instantiate the queue
        self.queue = queue.Queue(maxsize=self.max_queue_length)

        # Launch the listener in a separate thread
        self.start()

    def start(self):
        # Instantiate socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((self.host, self.port))

        # Launch listener
