import select
import socket
import sys
import time
import threading
import traceback

from .. import version

from .. import constants
from .. import exceptions as excp
from .. import utils

from ..utils import logger

class Client(object):
    """
    Client interface to the server.

    Attributes:
        _conn (socket.socket): The connection to the server.
        _listener (threading.Thread): The thread listening for responses
            from the server.
        _running (bool): Whether the client is running.
        _sent_requests (dict): The requests that have been sent to the
            server, but not yet responded to.
    """

    def __init__(self):
        self._conn = None
        self._listener = None
        self._running = False
        self._sent_requests = {}

    def _listen(self):
        """
        Listens for responses from the server.
        """
        while self._running:
            try:
                resp = self._conn.recv(1024)
                if not resp:
                    break
                resp
