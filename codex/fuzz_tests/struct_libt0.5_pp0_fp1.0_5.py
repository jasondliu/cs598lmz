import _struct

from . import _constants
from . import _enums
from . import _errors
from . import _types
from . import _utils


class _Connection(object):
    def __init__(self, connection):
        self._connection = connection


class _Cursor(_Connection):
    def __init__(self, connection):
        super(_Cursor, self).__init__(connection)
        self._description = None
        self._rowcount = -1
        self._arraysize = 1
        self._errorhandler = None
        self._messages = []

    def close(self):
        self._check_not_closed()
        self._connection = None

    def execute(self, operation, parameters=None):
        self._check_not_closed()
        self._check_no_result()
        self._errorhandler = None
        self._rowcount = -1
        self._description = None
        self._messages = []

        if parameters is None:
            parameters = ()

        if self._connection.autocommit:
            self._connection._begin
