import select
import socket
import time
import threading
import logging
import json

from . import config
from . import utils
from . import constants
from . import exceptions
from . import protocol
from . import transport

logger = logging.getLogger(__name__)

class Client(object):
    def __init__(self, host, port, timeout=None, transport_class=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.transport_class = transport_class or transport.TCPTransport
        self.transport = None
        self.protocol = None
        self.connection = None
        self.connected = False
        self.connecting = False
        self.connect_lock = threading.Lock()
        self.connect_cond = threading.Condition(self.connect_lock)
        self.connect_thread = None

    def connect(self):
        with self.connect_lock:
            if self.connected:
                return
            if self.connecting:
                self.connect_cond.wait
