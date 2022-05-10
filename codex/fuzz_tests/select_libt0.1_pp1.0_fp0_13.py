import select
import socket
import sys
import time
import traceback

from . import common
from . import config
from . import log
from . import util

class Server(object):
    def __init__(self, config_file):
        self.config = config.Config(config_file)
        self.log = log.Log(self.config)
        self.log.info("Starting server")
        self.log.info("Using config file: %s" % config_file)
        self.log.info("Using log file: %s" % self.config.log_file)
        self.log.info("Using pid file: %s" % self.config.pid_file)
        self.log.info("Using data directory: %s" % self.config.data_dir)
        self.log.info("Using port: %s" % self.config.port)
        self.log.info("Using max connections: %s" % self.config.max_connections)
        self.log.info("Using max message size: %s" % self.config.max_message
