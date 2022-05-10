import weakref

from . import _base
from . import _compat
from . import _util
from . import _types
from . import _errors
from . import _protocol


class _Cursor(_base.Cursor):
    """Cursor object for accessing the results of a query.

    The Cursor class represents a cursor to iterate over Mongo query results.
    """
