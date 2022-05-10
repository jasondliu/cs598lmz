import select
import socket
import sys
import time
import traceback

from . import config
from . import log
from . import util

__all__ = ['Server']

class Server(object):
    """A server that listens for connections from clients and dispatches
    requests to handlers.
    """

    def __init__(self, address, handler_factory,
                 log_level=log.INFO, log_file=None, log_max_size=None,
                 log_backup_count=None):
        self.address = address
        self.handler_factory = handler_factory
        self.log_level = log_level
        self.log_file = log_file
        self.log_max_size = log_max_size
        self.log_backup_count = log_backup_count
        self.running = False
        self.sock = None
        self.handlers = {}

    def start(self):
        """Start the server, listening for connections on the given address."""
        self.running = True
        self.log = log.Log
