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
