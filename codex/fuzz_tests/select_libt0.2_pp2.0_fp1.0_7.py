import selectors
import socket
import types

from . import utils
from . import config
from . import protocol
from . import exceptions
from . import log

logger = log.get_logger(__name__)


class Server:
    def __init__(self, host, port, handler, **kwargs):
        self.host = host
        self.port = port
        self.handler = handler
        self.selector = selectors.DefaultSelector()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((host, port))
        self.sock.listen()
        self.sock.setblocking(False)
        self.selector.register(self.sock, selectors.EVENT_READ, self.accept)
        self.clients = {}
        self.config = config.Config(**kwargs)

    def accept(self
