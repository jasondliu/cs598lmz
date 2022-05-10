import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import log
from . import util

#------------------------------------------------------------------------------

class Server(object):

    def __init__(self, config_file):
        self.config = config.Config(config_file)
        self.log = log.Log(self.config)
        self.db = common.Database(self.config, self.log)
        self.cache = common.Cache(self.config, self.log, self.db)
        self.server = None
        self.thread = None
        self.running = False

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.server:
            self.server.close()

    def run(self):
        self.log.info("Starting server.")
