import weakref

from . import _core
from . import _errors
from . import _util
from . import _config
from . import _compat
from . import _sqlite_lock
from . import _version


@_compat.register_sqlite3_adapter
def adapt_buffer(buffer):
    return buffer, _core.Buffer


@_compat.register_sqlite3_converter
def convert_buffer(buffer):
    return buffer


class Connection(_core.Connection):
    """
    A SQLite database connection.
    """

