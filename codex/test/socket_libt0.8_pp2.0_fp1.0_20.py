import socket
import sys
import threading
import logging
import datetime

from ..utility import util
from ..utility.configuration import Configuration
from ..utility import logger_manager
from . import server_proxy
from . import server_gateway
from . import server_monitor

import time

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

class MainServer():
    def __init__(self):
        logger_manager.setup_loggers(__name__)


        self.conf = Configuration()
        self.sock = None
        self.sock_2 = None
        self.s
