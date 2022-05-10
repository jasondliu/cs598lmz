import weakref

from . import pool


class Pool(object):
    """
    A connection pool that reuses existing connections.

    :param connection:
        A :class:`Connection <Connection>` instance.
    :param max_connections:
        The maximum number of connections to keep open in a pool.
    :param max_idle_time:
        The maximum number of seconds a connection can persist in the pool.
        Use this to avoid long periods of inactivity in your application.
    """
    def __init__(self, connection, max_connections=None, max_idle_time=None):
        self._connection = connection
        self._max_connections = max_connections or 10
        self._max_idle_time = max_idle_time
        self._max_idle_time_seconds = max_idle_time and max_idle_time.total_seconds()
        self._created_connections = 0
        self._available_connections = deque()
        self._in_use_connections = set()
        self._check_timeout = None
