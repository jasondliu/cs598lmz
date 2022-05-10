import _struct

from . import _const
from . import _util
from . import _compat

from . import _struct
from . import _util
from . import _compat

class _Cursor(object):
    """
    A cursor object.

    The cursor is used to traverse the records of a query result.
    """
    def __init__(self, connection, handle, arraysize):
        self._connection = connection
        self._handle = handle
        self._arraysize = arraysize
        self._description = None
        self._rowcount = -1
        self._rownumber = 0
        self._row = None
        self._error = None
        self._warnings = None
        self._closed = False

    def __del__(self):
        self.close()

    def close(self):
        """
        Close the cursor.

        The cursor is unusable from this point.
        """
        if self._closed:
            return
        self._closed = True
        self._handle = None
        self._connection = None

