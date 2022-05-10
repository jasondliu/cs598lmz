import select
import socket
import sys
import threading
import time

from . import config
from . import util

log = logging.getLogger(__name__)


class Server(object):
    """
    A server that listens for incoming connections and dispatches them to
    a handler.
    """
    def __init__(self, handler, port=None):
        self.handler = handler
        self.port = port or config.PORT
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('', self.port))
        self.server.listen(5)
        self.server.setblocking(0)
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            try:
                self.handle_connections()
            except KeyboardInterrupt:
                break
            except Exception:
                log.ex
