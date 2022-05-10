import select
import socket
import sys
import time

import numpy as np

from . import _common
from . import _constants
from . import _errors
from . import _transport
from . import _types
from . import _util

if sys.version_info >= (3, 0):
    from queue import Queue
else:
    from Queue import Queue


class _UDPTransport(object):
    def __init__(self, socket, timeout):
        self._socket = socket
        self._timeout = timeout
        self._last_receive_time = 0
        self._last_send_time = 0

    def send(self, data):
        self._socket.sendto(data, 0, (_constants.UDP_BROADCAST_IP, _constants.UDP_PORT))
        self._last_send_time = time.time()

    def receive(self):
        if time.time() - self._last_receive_time > self._timeout:
            self._last_receive_time = time.time()
            return None
       
