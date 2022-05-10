import select
import socket
import sys
import threading
import time
import traceback

import numpy as np

from bson import BSON

from ..utils import logging, misc

# Initialize the logger.
logger = logging.getLogger(__name__)


class Server(object):
    """
    A TCP server that receives data and runs a callback function.
    """

    def __init__(self, port, callback, timeout=1):
        """
        Initialize the server.

        Parameters
        ----------
        port : int
            The port number to listen on.
        callback : function
            The function to call when data is received.
        timeout : float, optional
            The timeout for receiving data.
        """

        # Store the arguments.
        self._port = port
        self._callback = callback
        self._timeout = timeout

        # Create the server socket.
