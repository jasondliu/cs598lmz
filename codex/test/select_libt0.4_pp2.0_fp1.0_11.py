import select
import socket
import sys
import threading
import time
import traceback

import numpy as np

from . import util
from . import config
from . import const
from . import log
from . import msg
from . import packet
from . import packet_pb2

class Client(object):
    """
    Client class for communicating with the server.
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.connect((self.host, self.port))
        self.socket.setblocking(0)
        self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

        self.inputs = [self.socket]
        self.outputs = []
