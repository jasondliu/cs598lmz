import socket
import sys
from time import sleep
import struct

from threading import Thread
from queue import Queue

import select

from random import random

from time import time

from socket import error as socket_error

#from OpenSSL import SSL

import logging
log = logging.getLogger(__name__)

BUFFER_SIZE = 4096

class Socket:
    def __init__(self, sock=None, timeout=None, debug=False):
        self.sock = sock
        self.debug = debug

        self.sock.settimeout(timeout)

        self.queue = Queue()

        self.thread = Thread(target=self.thread_run)
        self.thread.daemon = True
        self.thread.start()

    def connect(self, host, port):
        self.sock.connect((host, port))

    def close(self):
        self.sock.close()

    def send(self, data):
        log.debug("Sending: %s" % data)
        self.sock.send(data)


