import selectors
import socket
import types

from . import config
from . import protocol
from . import util
from . import version

_LOGGER = logging.getLogger(__name__)


class Connection(object):
    """
    A connection to a remote host.
    """

    def __init__(self, host, port, timeout=None):
        """
        Initialize a new connection to the specified host and port.

        :param host: The host to connect to.
        :type host: str
        :param port: The port to connect to.
        :type port: int
        :param timeout: The timeout for the connection.
        :type timeout: int
        """
        self.host = host
        self.port = port
        self.timeout = timeout

        self.socket = None

        self.selector = selectors.DefaultSelector()

        self.request_id = 0

        self.request_callbacks = {}

