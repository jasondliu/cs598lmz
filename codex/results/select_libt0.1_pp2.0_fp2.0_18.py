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
from . import util
from . import version

#-----------------------------------------------------------------------------
# Globals
#-----------------------------------------------------------------------------

_logger = log.get_logger(__name__)

#-----------------------------------------------------------------------------
# Classes
#-----------------------------------------------------------------------------

class _Connection(object):
    """
    A connection to a remote server.
    """

    def __init__(self, server, sock, addr):
        self.server = server
        self.sock = sock
        self.addr = addr
        self.closed = False
        self.last_activity = time.time()
        self.lock = threading.Lock()
        self.send_queue = []
        self.send_queue_size = 0
        self.send_queue_max_size = config.get_int('server', 'send_queue_max_size')
        self.send_queue_max_wait = config.get_
