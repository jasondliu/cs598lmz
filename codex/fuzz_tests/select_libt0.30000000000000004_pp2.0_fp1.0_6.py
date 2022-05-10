import select
import socket
import sys
import threading
import time
import traceback

from . import errors
from . import event
from . import log
from . import message
from . import util

class Connection(object):
    """
    A connection to a remote host.
    """

    def __init__(self, host, port, timeout=None):
        self._host = host
        self._port = port
        self._timeout = timeout

        self._socket = None
        self._socket_lock = threading.Lock()
        self._socket_event = threading.Event()

        self._recv_thread = None
        self._recv_thread_lock = threading.Lock()
        self._recv_thread_event = threading.Event()

        self._send_thread = None
        self._send_thread_lock = threading.Lock()
        self._send_thread_event = threading.Event()

        self._send_queue = collections.deque()
        self._send_queue_lock = threading.Lock()
        self._send_queue_event =
