import select
import socket
import sys
import time
import threading
import traceback

from . import util
from . import client
from . import server
from . import protocol
from . import config
from . import log
from . import error
from . import __version__

class Server(object):
    """
    The main server class.
    """

    def __init__(self, config):
        self.config = config
        self.log = log.get_logger(config)
        self.log.info("Starting server version %s", __version__)
        self.log.debug("Using config: %s", config)
        self.log.debug("Using log config: %s", log.get_log_config())
        self.log.debug("Using log level: %s", log.get_log_level())
        self.log.debug("Using log format: %s", log.get_log_format())
        self.log.debug("Using log file: %s", log.get_log_file())
        self.log.debug("Using log max size: %s",
