import weakref

from . import _compat
from . import _util
from . import _vendor
from . import _wrappers

__all__ = [
    'Cursor',
    'Connection',
    'ConnectionPool',
    'Pool',
    'PoolConnection',
    'PoolError',
    'PoolInterface',
    'TimeoutError',
]

logger = _compat.logging.getLogger(__name__)


class PoolError(Exception):
    """Base class for all connection pool exceptions."""


class TimeoutError(PoolError):
    """Raised when a connection pool times out on getting a connection."""


class PoolInterface(object):
    """Abstract base class for connection pools."""

    def getconn(self, *args, **kwargs):
        """Get a connection from the pool.

        The *args and **kwargs arguments are passed to the connection
        constructor.
        """
        raise NotImplementedError

