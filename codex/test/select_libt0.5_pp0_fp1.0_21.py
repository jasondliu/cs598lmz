import select
import socket
import sys
import threading
import time

from . import config
from . import log
from . import util

logger = log.get_logger()

class Client(object):
    """
    The Client class is responsible for connecting to a server, sending
    commands and handling the output.
    """

    def __init__(self, server, port, username, password):
        self.server = server
        self.port = port
        self.username = username
        self.password = password

        self.socket = None
        self.connected = False
        self.buffer = ""
        self.output_buffer = ""
        self.output_buffer_lock = threading.Lock()

        self.command_queue = []
        self.command_queue_lock = threading.Lock()

        self.output_listeners = []
        self.output_listeners_lock = threading.Lock()

        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

