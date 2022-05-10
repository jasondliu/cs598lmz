import select
import socket
import sys
import time
import threading
import traceback
import Queue

from . import common
from . import config
from . import log
from . import util

class Client(object):
    def __init__(self, host, port, name, password,
                 timeout=config.DEFAULT_TIMEOUT,
                 max_attempts=config.DEFAULT_MAX_ATTEMPTS,
                 retry_delay=config.DEFAULT_RETRY_DELAY,
                 log_level=config.DEFAULT_LOG_LEVEL):
        self.host = host
        self.port = port
