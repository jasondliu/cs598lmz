import select
import socket
import sys
import time
import threading
import re
import logging
import Queue

from . import common
from . import config
from . import errors
from . import event
from . import log
from . import message
from . import network
from . import protocol
from . import util

logger = logging.getLogger(__name__)

class Connection(object):
    """
    A connection to a remote host.

    :param host: The host to connect to.
    :param port: The port to connect to.
    :param ssl: Whether to use SSL.
    :param connect_timeout: The connection timeout.
    :param bind_address: The address to bind to.
    """
    def __init__(self, host, port, ssl=False, connect_timeout=None, bind_address=None):
        self.host = host
        self.port = port
        self.ssl = ssl
        self.connect_timeout = connect_timeout
        self.bind_address = bind_address
        self.socket = None
        self.connected =
