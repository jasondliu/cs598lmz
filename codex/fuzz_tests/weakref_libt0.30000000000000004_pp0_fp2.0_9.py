import weakref

from . import _core
from . import _util
from . import _interface

from . import _core
from . import _util
from . import _interface

class _Cursor(object):
    """
    A cursor is the mechanism used to traverse the records of a database
    table.  Cursors are created by the connection.cursor() method: they are
    bound to the connection for the entire lifetime and all the commands are
    executed in the context of the database session wrapped by the connection.
    """
    def __init__(self, connection):
        self._connection = weakref.proxy(connection)
        self._cursor = _core.cursor(self._connection._connection)
        self._description = None
        self._rowcount = -1
        self._arraysize = 1
        self._lastrowid = None
        self._rownumber = 0
        self._closed = False
        self._prefetch = 1
        self._outputsize = []
        self._inputsizes = []
        self._inputtypehandler = _interface.InputTypeHandler(self._c
