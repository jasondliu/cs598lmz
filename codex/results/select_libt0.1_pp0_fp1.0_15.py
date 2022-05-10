import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import errors
from . import log
from . import util
from . import version

# pylint: disable=too-many-lines

# pylint: disable=too-many-instance-attributes
class Server(object):
    """
    The main server class.
    """
    def __init__(self, config_file):
        """
        Initialize the server.
        """
        self.config_file = config_file
        self.config = config.Config(config_file)
        self.config.load()
        self.config.save()

        self.logger = log.get_logger(self.config.log_file,
                                     self.config.log_level,
                                     self.config.log_max_bytes,
                                     self.config.log_backup_count)

        self.logger.info("Starting %s version %s",
                         constants.PROGRAM_NAME
