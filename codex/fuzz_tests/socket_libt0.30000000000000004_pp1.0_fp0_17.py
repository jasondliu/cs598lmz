import socket
import sys
import threading
import time
import traceback

from . import utils
from . import constants
from . import exceptions
from . import log
from . import protocol
from . import transport
from . import types
from . import user_agent
from . import version

_LOGGER = log.get_logger(__name__)


class Connection(object):
    """
    A connection to a Cassandra cluster.

    Example usage::

        >>> from cassandra.cluster import Cluster
        >>> cluster = Cluster(['192.168.1.1', '192.168.1.2'])
        >>> session = cluster.connect()
        >>> session.set_keyspace("mykeyspace")
        >>> session.execute("SELECT * FROM mycf")
    """

    _lock = threading.Lock()
    _shutdown = False
    _listeners = {}

    _total_reqd_attempts = 0
    _total_reqd_timeouts = 0
    _total_reqd_errors = 0

    _total_reqd_connections = 0
    _
