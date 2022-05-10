import weakref

from . import _base
from . import _util
from . import _compat
from . import _errors
from . import _types


class _Cursor(_base.Cursor):
    """Cursor for a PostgreSQL connection.

    This class is not intended to be instantiated directly.
    Use :meth:`Connection.cursor` to create a cursor.
    """

    def __init__(self, connection):
        super(_Cursor, self).__init__(connection)
        self._pgconn = connection._pgconn
        self._pgres = None
        self._pgres_offset = None
        self._pgres_count = None
        self._pgres_status = None
        self._pgres_description = None
        self._pgres_row_count = None
        self._pgres_oid = None
        self._pgres_type = None
        self._pgres_is_binary = None
        self._pgres_is_text = None
        self._pgres_is_scrollable = None
