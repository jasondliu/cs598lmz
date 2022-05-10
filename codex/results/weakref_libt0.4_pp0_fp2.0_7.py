import weakref

from . import _wrappers
from . import _util
from . import _types
from . import _errors

from . import _lib


class _Cursor(object):
    """
    A cursor is used to iterate through the results of a query.

    .. versionadded:: 1.3
    """

    def __init__(self, session, query, params, result, timeout):
        self._session = weakref.ref(session)
        self._query = query
        self._params = params
        self._result = result
        self._timeout = timeout
        self._row_factory = None
        self._row_formatter = None
        self._column_names = None
        self._column_types = None
        self._consume_all = False
        self._consume_remaining = False
        self._buffer_rows = 0
        self._buffer = []
        self._buffer_index = 0
        self._prefetching_scheduled = False
        self._prefetching_lock = threading.Lock()
        self._row_count =
