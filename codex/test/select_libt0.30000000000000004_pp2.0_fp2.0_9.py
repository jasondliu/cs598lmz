import select
import socket
import sys
import threading
import time

from . import protocol
from . import util
from . import zmq_compat
from . import zmq_constants

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports

# System library imports

# Third-party imports

# Local imports

#-----------------------------------------------------------------------------
# Globals
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Functions
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Classes
#-----------------------------------------------------------------------------

class ZMQStream(object):
    """A tornado ZMQStream implementation.

    This class is a wrapper around a tornado IOLoop that interfaces with
    0MQ in a non-blocking manner.

    Parameters
    ----------
    socket : zmq.Socket
        The 0MQ socket to wrap.
    io_loop : tornado.ioloop.IOLoop
        The IOLoop to use for managing the 0MQ socket.
    """

    def __init__(self, socket, io_loop=None):
        self.socket = socket
        self.io_loop = io_
