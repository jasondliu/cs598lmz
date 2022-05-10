import select
import socket
import sys
import time

from . import common
from . import utils

logger = logging.getLogger(__name__)

class Server(object):
    def __init__(self, host, port, handler, timeout=None):
        self.host = host
        self.port = port
        self.handler = handler
        self.timeout = timeout
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((host, port))
        self.sock.listen(5)
        self.sock.setblocking(0)
        self.fd = self.sock.fileno()

    def run(self):
        inputs = [ self.fd ]
        outputs = []
        connections = {}
