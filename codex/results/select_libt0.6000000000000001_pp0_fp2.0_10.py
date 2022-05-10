import selectors
import signal

from . import log
from . import util
from .config import config
from .error import Error
from .message import Message
from .protocol import Protocol


class Connection(object):
    """
    A high-level representation of a connection to a p2p network.
    """
    def __init__(self, ip, port, protocol, selector=None, max_queue=None):
        self.ip = ip
        self.port = port
        self.protocol = protocol
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((ip, port))
        self.socket.setblocking(False)
        self.socket.listen(max_queue or config.get("p2p_max_queue"))
        self.selector = selector or selectors.DefaultSelector()
        self.selector.register(self.socket, selectors.EVENT_
