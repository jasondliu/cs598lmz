import select
import socket
import sys
import threading
import time

from . import config
from . import protocol
from . import util
from . import log
from . import exceptions

class Client(object):
    """
    A client for the ZeroTier network virtualization engine.
    """

    def __init__(self, config_path=None, log_file=None, log_level=None):
        """
        Initialize a ZeroTier Client.

        :param config_path: Path to a configuration file. If not specified,
            the default configuration path will be used.
        :param log_file: Path to a log file. If not specified, logging will be
            disabled.
        :param log_level: Logging level. If not specified, the default logging
            level will be used.
        """
        self.config = config.Config(config_path)
        self.logger = log.Logger(log_file, log_level)
        self.logger.info('Client initialized')

    def start(self):
        """
        Start the ZeroTier client.
        """
