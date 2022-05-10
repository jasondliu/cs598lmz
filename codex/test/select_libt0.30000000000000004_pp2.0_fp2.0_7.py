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
from . import log
from . import proxy
from . import utils
from . import version


class Server(object):
    """Proxy server.

    This class implements a proxy server. It listens for incoming
    connections and proxies the traffic to the destination server.

    """

    def __init__(self, config):
        """Constructor.

        The constructor creates a new server instance.

        Args:
            config: A config.Config instance.

        """
