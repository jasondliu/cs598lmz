import select
import socket
import sys
import threading
import time

from . import constants
from . import exceptions
from . import utils
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_lock = threading.Lock()
_g_sockets = {}


class _Socket(object):
    def __init__(self, sock, addr):
        self.sock = sock
        self.addr = addr
        self.last_active_time = time.time()
        self.recv_buf = b''
        self.send_buf = b''
        self.send_lock = threading.Lock()
        self.send_event = threading.Event()
        self.send_thread = threading.Thread(target=self._send_thread)
        self.send_thread.start()

    def _send_thread(self):
        while True:
            self.send_event.wait()
            self.send_event.clear()
            if not self.send_buf:
                continue
            try:
