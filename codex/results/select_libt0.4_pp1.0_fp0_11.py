import select
import socket
import sys
import time
import random
import logging

from . import __version__
from . import util
from . import const
from . import protocol
from . import error
from . import logger

def _get_logger():
    return logging.getLogger(__name__)

class Client(object):
    def __init__(self, host, port, timeout=None, logger=None):
        self._host = host
        self._port = port
        self._timeout = timeout
        self._socket = None
        self._logger = logger or _get_logger()

    def connect(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.settimeout(self._timeout)
        self._socket.connect((self._host, self._port))

    def disconnect(self):
        self._socket.close()
        self._socket = None

    def _send(self, request):
        self._logger.debug('send: %s', request)
        self._socket
