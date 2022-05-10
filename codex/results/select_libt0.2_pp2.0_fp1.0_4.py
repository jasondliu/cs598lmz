import select
import socket
import sys
import threading
import time

from . import config
from . import log
from . import util

logger = log.get_logger()

class Server(object):
    def __init__(self, host, port, handler):
        self.host = host
        self.port = port
        self.handler = handler
        self.server = None

    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        self.server.listen(config.SERVER_BACKLOG)
        logger.info('Listening on %s:%d' % (self.host, self.port))

        while True:
            try:
                client, address = self.server.accept()
                logger.info('Accepted connection from %s:%d' % address)
                threading
