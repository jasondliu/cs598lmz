import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import pwd
import grp
import re

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from lib.config import Config
from lib.logger import Logger
from lib.daemon import Daemon
from lib.database import Database
from lib.network import Network
from lib.utils import Utils
from lib.sensor import Sensor

class SensorDaemon(Daemon):
    def __init__(self, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
        Daemon.__init__(self, pidfile, stdin, stdout, stderr)
        self.config = Config()
        self.logger = Logger(self.config.get('log_file'), self.config.get('log_level'))
        self.utils = Utils()
        self.sensor = Sensor(self.config, self.logger)

    def run(self):
        self.logger.info('Starting sensor')
        self
