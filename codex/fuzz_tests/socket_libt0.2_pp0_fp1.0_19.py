import socket
import sys
import time

from . import config
from . import utils
from . import version

_logger = logging.getLogger(__name__)


class Client(object):
    """
    A client for the StatsD server.

    >>> client = Client('localhost', 8125)
    >>> client.incr('some.int')
    >>> client.decr('some.int')
    >>> client.timing('some.timer', 500)
    >>> client.timing('some.timer', 500)
    >>> client.gauge('some.gauge', 42)
    >>> client.gauge('some.gauge', 42)
    >>> client.gauge('some.gauge', -42)
    >>> client.gauge('some.gauge', -42)
    >>> client.gauge('some.gauge', 0)
    >>> client.gauge('some.gauge', 0)
    >>> client.histogram('some.histogram', 42)
    >>> client.histogram('some.histogram',
