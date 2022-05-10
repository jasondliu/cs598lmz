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

#
# Constants
#

#
# Globals
#

#
# Functions
#

def _get_socket_path():
    """
    Get the path to the socket file.
    """
    return os.path.join(config.get_config_dir(), 'socket')

def _get_socket_path_old():
    """
    Get the path to the old socket file.
    """
    return os.path.join(config.get_config_dir(), 'socket.old')

def _get_socket_path_tmp():
    """
    Get the path to the temporary socket file.
    """
    return os.path.join(config.get_config_dir(), 'socket.tmp')

def _get_socket_path_tmp_old():
