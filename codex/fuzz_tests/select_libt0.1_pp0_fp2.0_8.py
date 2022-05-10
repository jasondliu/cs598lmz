import select
import socket
import sys
import threading
import time
import traceback

from . import constants
from . import exceptions
from . import utils
from . import version
from . import wire
from . import wire_format
from . import wire_constants
from . import wire_types

_logger = logging.getLogger(__name__)


class Connection(object):
    """
    A connection to a remote host.

    :param host: The host to connect to.
    :type host: str
    :param port: The port to connect to.
    :type port: int
    :param timeout: The timeout for the connection.
    :type timeout: float
    :param ssl_context: The SSL context to use for the connection.
    :type ssl_context: ssl.SSLContext
    :param ssl_hostname: The hostname to use for the SSL connection.
    :type ssl_hostname: str
    :param ssl_cafile: The CA file to use for the SSL connection.
    :type ssl_cafile: str

