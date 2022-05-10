import weakref

from . import _base
from . import _compat
from . import _util
from . import _types


class _Connection(object):
    """
    A connection to a database.

    The connection object is **not** thread-safe.
    """
    def __init__(self, connection):
        self._connection = connection

    def __del__(self):
        self.close()

    def close(self):
        """
        Close the connection.
        """
        if self._connection is not None:
            self._connection.close()
            self._connection = None

    def commit(self):
        """
        Commit the current transaction.
        """
        self._connection.commit()

