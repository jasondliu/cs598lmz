import selectors
import traceback
import subprocess
import sys
import os
import time
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../python"))

from lib.logger import Logger
from lib.config import Config
from lib.client import Client
from lib.daemon import Daemon
from lib.helpers import Helpers

PID_FILE = 'pid'
NAME = 'client'

class ClientDaemon(Daemon):
    def run(self):
        config = Config()
        logger = Logger(config.log_level, config.log_file)
        client = Client(config, logger)
        helpers = Helpers(config, logger)

        logger.log(config.log_level, 'Started {} daemon [{}] v{}'.format(NAME, config.project, config.version))

        selector = selectors.DefaultSelector()


