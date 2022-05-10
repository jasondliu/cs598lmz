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
from . import events
from . import log
from . import messages
from . import util
from . import version

#-------------------------------------------------------------------------------

class Client(object):
    """
    A client for the MUD server.
    """

    def __init__(self, host, port, name, password,
                 encoding=constants.DEFAULT_ENCODING,
                 timeout=constants.DEFAULT_TIMEOUT,
                 reconnect=constants.DEFAULT_RECONNECT,
                 reconnect_wait=constants.DEFAULT_RECONNECT_WAIT,
                 reconnect_max_wait=constants.DEFAULT_RECONNECT_MAX_WAIT,
                 reconnect_max_attempts=constants.DEFAULT_RECONNECT_MAX_ATTEMPTS,
                 reconnect_jitter=constants.DEFAULT_RECONNECT_JITTER,
                 reconnect_jitter_wait=constants.DEFAULT_RECON
