import ctypes
import ctypes.util
import threading
import sqlite3 as sqlite

import struct


class ZMQ(object):
    """
    This class provides a simple interface to ZeroMQ
    """

    # Timeout in seconds
    TIMEOUT = 5

    # Port to use
    PORT = 8080

    # Port to use
    HOST = "0.0.0.0"

    def __init__(self, data_file=None, context_factory=None):
        """
        Connect to the ZeroMQ server, if a context_factory is not provided,
        it is created.
        """
        self.data_file = data_file
        self.context = context_factory if context_factory is not None else zmq.Context()
        # Create a REQ socket
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://%s:%d" % (self.HOST, self.PORT))
        # Set a timeout
        self.socket.setsockopt(zmq.LINGER, self.TIMEOUT * 1000)

   
