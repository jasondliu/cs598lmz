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
