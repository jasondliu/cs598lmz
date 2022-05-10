import socket
import sys
import time
import threading
import logging
import os
import signal
import subprocess

from . import config
from . import utils
from . import exceptions
from . import constants
from . import __version__
from . import __author__
from . import __email__
from . import __license__
from . import __url__
from . import __description__

logger = logging.getLogger(__name__)


class Server(object):
    """
    The server class.
    """

    def __init__(self, host, port, config_file, debug=False):
        self.host = host
        self.port = port
        self.config_file = config_file
        self.debug = debug

        self.config = config.Config(self.config_file)
        self.config.load()

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       
