import threading
# Test threading daemon
import time

from lib.logger import logger
from lib.config import config
from lib.common import common

from lib.plugin import plugin

class plugin_thread(threading.Thread):
    def __init__(self, threadID, name, counter, plugin):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.plugin = plugin
    def run(self):
        #logger.info("Starting " + self.name)
        self.plugin.run()
        #logger.info("Exiting " + self.name)

class plugin_manager(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.plugins = []
        self.plugin_threads = []
    def run(self):
        logger.info("Starting " + self.name)
       
