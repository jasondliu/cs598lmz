import weakref

from . import _base
from . import _compat
from . import _util
from . import _vendor
from . import _version
from . import exceptions
from . import interfaces

__all__ = [
    'Connection',
    'ConnectionPool',
    'Pool',
    'PoolConnection',
    'PoolListener',
    'TornadoConnection',
]


class Connection(_base.Connection):
    """A connection to a PostgreSQL server.

    The :class:`Connection` class represents a single connection to a
    PostgreSQL server.  A connection is associated with a cursor, which
    sends queries to the server and returns the results.  The connection
    also maintains transaction state and manages the PostgreSQL notice
    processing.

    The :class:`Connection` class is *not* thread-safe.  If you want to use
    a connection from multiple threads at once, then use a separate
    :class:`Connection` object in each thread.  Alternatively, you can use
    a :class:`ConnectionPool` object, which manages a pool of connections
    that can be shared by multiple threads
