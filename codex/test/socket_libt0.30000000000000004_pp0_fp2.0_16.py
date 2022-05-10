import socket
import sys
import time
import traceback
import threading

from . import config
from . import log
from . import util
from . import version

class Client(object):
    def __init__(self, host, port, username, password,
                 timeout=config.DEFAULT_TIMEOUT,
                 reconnect=config.DEFAULT_RECONNECT,
                 reconnect_wait=config.DEFAULT_RECONNECT_WAIT):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.timeout = timeout
        self.reconnect = reconnect
        self.reconnect_wait = reconnect_wait
        self.sock = None
        self.connected = False
        self.connect_lock = threading.Lock()
        self.connect()

    def connect(self):
        with self.connect_lock:
            if self.connected:
                return
