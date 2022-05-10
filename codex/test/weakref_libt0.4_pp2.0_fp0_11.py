import weakref

from . import _base
from .. import _util

from .._util import _decode_string, _encode_string

class _Connection(_base.Connection):
    """
    A connection to a PostgreSQL database.

    This class is primarily intended for internal use.
    """

    def __init__(self, *args, **kwargs):
        """
        Create a new connection to a PostgreSQL database.

        The arguments are the same as for the :class:`~psycopg2.connect`
        function.
        """

        self._connection = psycopg2.connect(*args, **kwargs)
        self._cursor = self._connection.cursor()

    def _execute(self, sql, params=None):
        self._cursor.execute(sql, params)

    def _executemany(self, sql, params=None):
        self._cursor.executemany(sql, params)

    def _fetchone(self):
        return self._cursor.fetchone()

