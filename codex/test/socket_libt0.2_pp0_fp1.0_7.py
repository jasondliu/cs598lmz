import socket
import sys
import time
import threading
import traceback
import uuid

from . import common
from . import config
from . import log
from . import message
from . import util
from . import zmq

class Client(object):
    def __init__(self, config, log):
        self.config = config
        self.log = log
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.DEALER)
        self.socket.setsockopt(zmq.IDENTITY, self.config.client_id)
        self.socket.setsockopt(zmq.LINGER, 0)
        self.socket.connect(self.config.server_address)
        self.log.info('Connected to server at %s', self.config.server_address)
        self.poller = zmq.Poller()
        self.poller.register(self.socket, zmq.POLLIN)
        self.running = False
        self.thread = None
