import select
import socket
import sys
import time
import traceback

from . import common
from . import config
from . import log
from . import util
from . import version

from .common import *
from .config import *
from .log import *
from .util import *
from .version import *

class Server(object):
    def __init__(self, config):
        self.config = config
        self.log = log.Log(config)
        self.log.info("Starting server")
        self.log.info("Version: %s" % version.VERSION)
        self.log.info("Config: %s" % config.config_file)
        self.log.info("Log: %s" % config.log_file)
        self.log.info("PID: %s" % config.pid_file)
        self.log.info("Data: %s" % config.data_dir)
