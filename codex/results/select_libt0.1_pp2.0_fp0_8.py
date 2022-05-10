import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import exceptions
from . import log
from . import utils
from . import version

# pylint: disable=too-many-lines

_LOGGER = log.get_logger(__name__)

# pylint: disable=too-many-instance-attributes
class Server(object):
    """
    The server class.
    """

    def __init__(self, config_file, config_dict=None):
        """
        Initialize the server.
        """
        self.config_file = config_file
        self.config_dict = config_dict
        self.config = None
        self.config_lock = threading.Lock()
        self.config_thread = None
        self.config_thread_stop = threading.Event()
        self.config_thread_reload = threading.Event()
        self.config_thread_reload.set()
        self.config_thread_
