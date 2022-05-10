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
    The Server class is the main class of the server. It is responsible for
    starting and stopping the server, as well as handling all of the
    connections.
    """

    def __init__(self, config_file=None):
        """
        Initializes the server.

        :param config_file: The path to the configuration file to use.
        :type config_file: str
        """

        self.config_file = config_file
        self.config = config.Config(self.config_file)

        self.logger = log.Logger(self.config.get('log_file'),
                                 self.config.get('log_level'))

        self.logger
