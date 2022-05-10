import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import util

# -----------------------------------------------------------------------------
#
# SERVER CLASS
#
# -----------------------------------------------------------------------------

class Server(object):
    """
    The Server class is the main class of the server. It is responsible for
    listening for connections, accepting them, and spawning a new thread to
    handle each connection.
    """

    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

        self.sock = None
        self.threads = []

