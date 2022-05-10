import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import errors
from . import util

#------------------------------------------------------------------------------
# Logging
#------------------------------------------------------------------------------

logger = logging.getLogger(__name__)

#------------------------------------------------------------------------------
# TCP Socket
#------------------------------------------------------------------------------

class TCPSocket(object):
    """
    A TCP socket.
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None

    def __repr__(self):
        return '<TCPSocket(%s:%s)>' % (self.host, self.port)

    def __str__(self):
        return '%s:%s' % (self.host, self.port)

    def __eq__(self, other):
        return self.host == other.host and self.port == other.port

    def __hash__(self):
        return hash(self.host) ^ hash(self.port)
