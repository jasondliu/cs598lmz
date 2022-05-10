import selectors
import socket
import types

from threading import Thread
from time import sleep
from threading import Lock
from src.server.utils import get_logger, get_config
from src.server.protocol import ProtocolServer
from src.server.database import Database
from src.server.cache import Cache
from src.server.protocol import ProtocolServer

logger = get_logger(__name__)
config = get_config()

class Server:
    def __init__(self):
        self.sel = selectors.DefaultSelector()
        self.host = config['server']['host']
        self.port = int(config['server']['port'])
        self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.lsock.bind((self.host, self.port))
        self.lsock.listen(100)
        self.lsock.setblocking
