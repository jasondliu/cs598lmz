import select
import socket
import sys
import threading
import time

from . import __version__
from . import config
from . import log
from . import util
from . import version

logger = log.get_logger(__name__)


class Server(object):
    """
    The server class.
    """
    def __init__(self, config_file, debug=False):
        config.load_config(config_file)
        self.debug = debug
        self.sock = None
        self.listening = False
        self.shutting_down = False
        self.thread = None
        self.client_threads = []
        self.client_threads_lock = threading.Lock()
        self.client_threads_cv = threading.Condition(self.client_threads_lock)
        self.client_threads_done = []
        self.client_threads_done_lock = threading.Lock()
        self.client_threads_done_cv = threading.Condition(self.client_threads_done_lock)
