import select
import socket
import time
import sys

from . import common
from . import settings
from . import utils

logger = logging.getLogger(__name__)

class Server(object):
    def __init__(self, address, port, database):
        self.address = address
        self.port = port
        self.database = database
        self.clients = {}
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((address, port))
        self.server_socket.listen(10)
        self.server_socket.setblocking(0)

        self.epoll = select.epoll()
        self.epoll.register(self.server_socket.fileno(), select.EPOLLIN)
