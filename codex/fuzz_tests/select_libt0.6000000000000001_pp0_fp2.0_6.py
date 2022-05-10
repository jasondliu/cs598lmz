import select
import sys
import threading

from server import *
from client import *

import libs.common as common
from libs.common import *
from libs.utils import *

class Tunnel(object):
    """
    The Tunnel class is used for the initialization of the tunnel.
    """
    def __init__(self, tunnel_type, host, port, verbose, timeout, data_size):
        """
        Initialize the tunnel object.

        @param tunnel_type: the tunnel type, 'client' or 'server'.
        @param host: the host of the server.
        @param port: the port of the server.
        @param verbose: the verbose level.
        @param timeout: the timeout value.
        @param data_size: the data size.
        """
        self.tunnel_type = tunnel_type
        self.host = host
        self.port = port
        self.verbose = verbose
        self.timeout = timeout
        self.data_size = data_size

    def start(self):
        """
        Start the tunnel
