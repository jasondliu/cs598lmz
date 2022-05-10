import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import log
from . import util

class Server(object):
    def __init__(self, config_file):
        self.config = config.Config(config_file)
        self.logger = log.Logger(self.config)
        self.logger.info("Starting server")
        self.logger.info("Using config file %s" % config_file)
        self.logger.info("Using log file %s" % self.config.log_file)
        self.logger.info("Using pid file %s" % self.config.pid_file)
        self.logger.info("Using socket file %s" % self.config.socket_file)
        self.logger.info("Using data directory %s" % self.config.data_dir)
        self.logger.info("Using max connections %d" % self.config.max_connections)
        self.logger.info("
