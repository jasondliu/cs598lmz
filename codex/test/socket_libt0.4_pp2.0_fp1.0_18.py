import socket
import threading
import time

from . import _discovery
from . import _utils

_logger = logging.getLogger(__name__)


class DiscoveryError(Exception):
    """Base class for discovery errors."""


class NoServersFoundError(DiscoveryError):
    """Raised when no servers are found."""


class ServerNotFoundError(DiscoveryError):
    """Raised when a server is not found."""


class ServerNotRespondingError(DiscoveryError):
    """Raised when a server is not responding."""


class ServerError(DiscoveryError):
    """Raised when a server returns an error."""


class Server(object):
    """Represents a server."""

    def __init__(self, ip, port, name=None):
        self.ip = ip
        self.port = port
        self.name = name

    def __repr__(self):
        return '<Server {self.ip}:{self.port}>'.format(self=self)

