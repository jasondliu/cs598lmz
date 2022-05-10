import selectors
import socket
import types
import time
from threading import Thread
from threading import Timer
from queue import Queue
from queue import Empty
import logging
import sys
from logging.handlers import RotatingFileHandler

from . import config
from . import utils
from . import exceptions
from . import http_parser
from . import http_request
from . import http_response
from . import http_connection
from . import http_connection_pool

class HttpServer:
    def __init__(self, host=None, port=None, workers=1, timeout=1,
                 keep_alive=True, keep_alive_timeout=300,
                 log_level=logging.INFO, log_file=None):
        self.host = host or config.HOST
        self.port = port or config.PORT
        self.workers = workers or config.WORKERS
        self.timeout = timeout or config.TIMEOUT
        self.keep_alive = keep_alive or config.KEEP_ALIVE
        self.keep_alive_timeout = keep_alive
