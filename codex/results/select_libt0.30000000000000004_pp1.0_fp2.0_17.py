import select
import socket
import sys
import threading
import time

from . import base
from . import config
from . import constants
from . import errors
from . import events
from . import logger
from . import protocol
from . import util
from . import version

from . import _thread_local
from . import _util
from . import _websocket_client

__all__ = ['Client']

_LOGGER = logger.get_logger(__name__)


def _create_connection(host, port, use_ssl, timeout, source_address=None):
    """Create a TCP connection to a host on a given port.

    Args:
        host (str): Hostname or IP address to connect to.
        port (int): Port to connect to.
        use_ssl (bool): If True, create the connection over SSL.
        timeout (float): Number of seconds to wait for the connection to succeed.
        source_address (tuple): Local address to bind to as a tuple (host, port).

    Returns:
        socket.socket: A socket object connected to the given host and
