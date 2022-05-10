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
    handling the main loop, accepting connections, and dispatching them to
    the appropriate handler.
    """

    def __init__(self, config_file=None, config_dict=None,
                 config_overrides=None, log_file=None, log_level=None,
                 log_format=None, log_date_format=None, log_color=None,
                 log_max_size=None, log_max_backups=None, log_max_age=None,
                 log_compress=None, log_console=None, log_console_level=None,
                 log_console_
