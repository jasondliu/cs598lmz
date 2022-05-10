import socket
import sys
import threading
import time

from . import config
from . import log
from . import utils
from . import version

logger = log.get_logger(__name__)


class Server(object):
    def __init__(self, host, port, handler):
        self.host = host
        self.port = port
        self.handler = handler
        self.server = None
        self.thread = None

    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        self.server.listen(5)

        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

