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

    def __init__(self, database, timeout=5.0, detect_types=0,
                 isolation_level=None, check_same_thread=True,
                 factory=None, cached_statements=100, uri=False,
                 **kwargs):
        """
        Open a new connection to a SQLite database file.

        :param str database:
            File name of the database file to open, or ``:memory:`` to open a
            new database connection to a database held in RAM.
        :param float timeout:
