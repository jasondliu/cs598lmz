import select
import socket
import sys
import threading
import time

from . import command
from . import logger
from . import network
from . import tcp


class Client(object):
    """
    A client that can connect to a server.
    """

    def __init__(self, address):
        self.address = address
        self.connection = None
        self.reader = None
        self.writer = None
        self.running = False
        self.recv_thread = None
        self.send_thread = None
        self.send_queue = queue.Queue()
        self.recv_queue = queue.Queue()
        self.recv_thread_lock = threading.Lock()
        self.send_thread_lock = threading.Lock()
        self.logger = logger.get_logger(__name__, 'client')
        self.logger.debug('Client initialized.')

