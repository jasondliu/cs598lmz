import select
import socket
import sys
import time
import traceback

import numpy as np

from . import constants
from . import exceptions
from . import messages
from . import utils
from . import version

logger = logging.getLogger(__name__)


class Client(object):
    """
    A client for communicating with a server.

    Parameters
    ----------
    host : str
        The hostname of the server.
    port : int
        The port of the server.
    timeout : float
        The timeout for the client.
    """

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.socket = None
        self.connected = False
        self.version = None
        self.server_version = None
        self.server_name = None
        self.server_description = None
        self.server_author = None
        self.server_license = None
        self.server_url = None
        self.server_timezone = None
