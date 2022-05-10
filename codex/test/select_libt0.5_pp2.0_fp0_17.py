import select

from . import utils
from . import network
from . import exceptions
from . import constants
from . import record
from . import __version__
from . import logger

logger = logger.getChild(__name__)

class Client(object):
    """
    A client for the Minecraft server.

    :param str host: The hostname of the server.
    :param int port: The port of the server.
    :param str username: The username of the user.
    :param str password: The password of the user.
    """

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

        self._protocol_version = None
        self._connection = network.Connection(self.host, self.port)
        self._connection.connect()

        self._handshake()

        self._login()
        self._ping()

    def _handshake(self):
        """
        Handshakes with the server.
        """

        self
