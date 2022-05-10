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
        self._config = config
        self._logger = log.get_logger(__name__)
        self._proxy = proxy.Proxy(config)
        self._server_socket = None
        self._server_thread = None
        self._shutdown_event = threading.Event()

    def start(self):
        """Start the server.

        This method starts the server. It creates a server socket,
        binds it to the configured address and port, and starts
