import select
import socket
import sys
import time
import threading
import traceback

import pymysql
import pymysql.cursors

from . import config
from . import log
from . import util
from . import version

logger = log.get_logger()

class Server(object):
    def __init__(self, config_file):
        self.config = config.Config(config_file)
        self.config.load()

        self.server_socket = None
        self.client_sockets = {}
        self.client_threads = {}
        self.client_thread_lock = threading.Lock()

        self.db_connection = None
        self.db_cursor = None

        self.stop_event = threading.Event()

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.
