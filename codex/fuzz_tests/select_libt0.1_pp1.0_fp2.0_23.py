import select
import socket
import sys
import time
import traceback

from . import config
from . import log
from . import util
from . import version

logger = log.get_logger(__name__)

class Server(object):
    def __init__(self, config_file, config_overrides=None):
        self.config = config.Config(config_file, config_overrides)
        self.sock = None
        self.clients = {}
        self.client_count = 0
        self.client_count_lock = threading.Lock()
        self.client_count_cond = threading.Condition(self.client_count_lock)
        self.client_count_max = self.config.get_int('server', 'max_clients')
        self.client_count_max_lock = threading.Lock()
        self.client_count_max_cond = threading.Condition(self.client_count_max_lock)
        self.client_count_max_changed = False
        self.client_count_max_changed
