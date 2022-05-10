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
