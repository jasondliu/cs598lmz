import socket
import sys
import threading
import time
import traceback
import urllib

import lib.config as config
import lib.info as info
import lib.logger
import lib.message as message
import lib.plugin as plugin
import lib.utils as utils

from lib.logger import log

class Bot(object):
    def __init__(self, config_file):
        self.config = config.Config(config_file)
        self.info = info.Info()
        self.plugins = plugin.PluginManager(self)
        self.message_handler = message.MessageHandler(self)
        self.socket = None
        self.socket_lock = threading.Lock()
        self.connect_lock = threading.Lock()
        self.connect_lock.acquire()
        self.connected = False
        self.running = False
        self.reconnect_delay = self.config.reconnect_delay
        self.reconnect_delay_step = self.config.reconnect_delay_step
        self.reconnect_delay_max = self.config.re
