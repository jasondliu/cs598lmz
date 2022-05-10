import select
import asyncio
import threading
import time
import json
import logging

from . import utils
from . import const
from . import exceptions
from . import protocol
from .log import logger

class Connection(object):
    def __init__(self, host, port, timeout=const.DEFAULT_TIMEOUT):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = None
        self.reader = None
        self.writer = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(False)

        try:
            self.sock.connect((self.host, self.port))
        except BlockingIOError:
            pass

        self.reader, self.writer = await_socket(self.sock, self.timeout)

    def close(self):
        if self.writer:
            self.writer.close()
