import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import utils
from . import version
from . import web

from . import __version__

logger = log.get_logger(__name__)

class Server(object):
    def __init__(self, config):
        self.config = config
        self.running = False
        self.sock = None
        self.web = None
        self.threads = []

    def start(self):
        self.running = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setblocking(0)
        self.sock.bind(('', self.config['port']))
        self.sock.listen(5)
