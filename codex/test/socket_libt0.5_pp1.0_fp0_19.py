import socket
import sys
import threading
import time
import traceback

from . import errors, exceptions, util
from .config import Config
from .message import Message
from .peer import Peer
from .peer_list import PeerList
from .ping import Ping
from .protocol import Protocol
from .thread import Thread

logger = logging.getLogger(__name__)


class Node(Thread):
    """
    This class implements the node.

    A node is a peer that can connect to other peers.
    """

    def __init__(self, config: Config) -> None:
        """
        Initialize a Node.

        Args:
            config: The configuration to use.
        """
        super().__init__()
        self.config = config
        self.protocol = Protocol(self)
        self.peer_list = PeerList(self.config)
        self.is_valid = False
        self.is_running = False
        self.is_stopping = False
        self.lock = threading.Lock()
        self.ping = Ping(self)
       
