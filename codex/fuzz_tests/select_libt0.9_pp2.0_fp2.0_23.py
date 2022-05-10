import select
import socket, pdb
import time
import types

from pika import exceptions
from pika import spec
from pika import channel
from pika import utils



# Global status flag
_stopped = False  # Set to True to stop/exit Pika


class AsyncoreConnection(object):
    """Asyncore Connection class

    Parameters:

        pika.ConnectionParameters parameters
            The connection parameters object

        pika.Channel channel_factory
            The channel factory

    """
    READ_ONLY = select.EPOLLIN | select.EPOLLPRI | select.EPOLLHUP | select.EPOLLRDHUP
    READ_WRITE = READ_ONLY | select.EPOLLOUT

    def __init__(self, parameters=None, channel_factory=None):
        """Create a new instance of the Connection object."""
        self.parameters = parameters or pika.ConnectionParameters()
        self._channels = {}
        self.connection_state = None
        self.io_loop = None
        self.ioloop_timeout =
