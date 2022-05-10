import select
import socket
import sys
import threading
import time

from . import common
from . import config
from . import log
from . import util

class Server(object):
    def __init__(self, config):
        self.config = config
        self.log = log.get_logger(self)
        self.sock = None
        self.thread = None
        self.clients = {}
        self.client_lock = threading.Lock()
        self.client_id = 0
        self.client_id_lock = threading.Lock()
