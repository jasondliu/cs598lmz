import socket
import sys
import time
import threading

from . import config
from . import log
from . import utils
from . import version
from . import worker

logger = log.get_logger(__name__)

class Server(object):
    def __init__(self, config, worker_class=worker.Worker):
        self.config = config
        self.worker_class = worker_class
        self.worker = None
        self.socket = None
        self.thread = None

    def start(self):
        self.worker = self.worker_class(self.config)
        self.worker.start()

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.config.host, self.config.port))
        self.socket.listen(self.config.backlog)

        self.thread = threading.Thread(target=self
