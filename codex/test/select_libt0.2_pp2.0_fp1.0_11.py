import select
import socket
import sys
import time
import traceback

from . import common
from . import config
from . import log
from . import util
from . import version

#------------------------------------------------------------------------------

class Server(object):
    """
    The server class.
    """

    #--------------------------------------------------------------------------
    # Public API
    #--------------------------------------------------------------------------

    def __init__(self, config_path):
        """
        Constructor.

        :param config_path: Path to the server configuration file.
        :type config_path: str

        :raises common.ConfigError: If the configuration file is invalid.
        """

        self._config = config.Config(config_path)
        self._logger = log.get_server_logger(self._config)
        self._logger.info("Starting server version %s", version.VERSION)

        self._sock = None
        self._clients = {}
        self._client_lock = threading.Lock()
        self._client_id_counter = 0

        self._running = False
        self._stop_event = threading.Event
