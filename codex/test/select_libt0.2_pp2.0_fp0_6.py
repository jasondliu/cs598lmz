import select
import socket
import sys
import time
import threading
import traceback

from . import common
from . import config
from . import log
from . import util
from . import version

class Server(object):
    def __init__(self, config):
        self.config = config
        self.log = log.get_logger('server')
        self.log.info('starting server')
        self.log.info('version %s', version.VERSION)
        self.log.info('config: %s', self.config)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((config.host, config.port))
        self.sock.listen(1)

        self.connections = {}
