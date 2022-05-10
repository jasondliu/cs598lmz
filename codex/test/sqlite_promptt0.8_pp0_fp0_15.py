import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:/Users/david/Documents/projects/tests/realtime/realtime.db')
import time
from multiprocessing import Process
from multiprocessing.connection import Client
import signal
from uinput import Keys
import os
from lxml import etree
import logging
from logging import handlers
from Queue import Queue

from realtime import config


class BaseClass(object):
    """
    A base class with a logger
    """
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)


class Config(BaseClass):
    """
    A wrapper class for the config module
    """
    def __init__(self):
        super(Config, self).__init__()
        self._config = config.Config()

        # Create the config dict
        self.config_dict = self._config.config_dict

    def get_config(self):
        return self.config_dict

