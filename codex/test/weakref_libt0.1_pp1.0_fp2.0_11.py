import weakref

from . import _base
from . import _util
from . import _types
from . import _errors
from . import _constants
from . import _lib
from . import _ffi
from . import _compat

__all__ = ['Connection', 'connect', 'ConnectionPool', 'connect_thread_safe']


class Connection(_base.Connection):
    """
    A connection to a PostgreSQL database.

    The connection is created by calling the :func:`connect` function.
    """

    def __init__(self, dsn, **kwargs):
        super(Connection, self).__init__(**kwargs)
        self._dsn = dsn
        self._conn = None
        self._closed = False
        self._protocol = 3
        self._encoding = 'utf-8'
        self._transaction_status = _constants.TRANSACTION_STATUS_IDLE
        self._isolation_level = _constants.ISOLATION_LEVEL_DEFAULT
        self._notices = []
        self._notice_handler = None
       
