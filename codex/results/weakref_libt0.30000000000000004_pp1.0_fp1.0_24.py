import weakref

from . import _base
from . import _common
from . import _compat
from . import _errors
from . import _util


class _Cursor(_base.Cursor):
    """Cursor object for accessing the results of a query.

    Cursors are not isolated, i.e., any changes done to the database by a
    cursor are immediately visible by other cursors or connections.

    Cursors keep a reference to their connection and thus keep the
    transaction alive for as long as the cursor lives.

    Do not create cursors manually, use :meth:`Connection.cursor` instead.
    """

    def __init__(self, connection):
        super(_Cursor, self).__init__(connection)
        self._description = None
        self._rowcount = -1
        self._arraysize = 1
        self._rownumber = 0
        self._lastrowid = None
        self._results = None
        self._result_pos = 0
        self._query_start_time = None
        self._query_end_time = None
        self._query
