import ctypes
import ctypes.util
import threading
import sqlite3
import abc
from ..sqlite_util import sqlite3_enable_load_extension, \
    sqlite3_load_extension, sqlite3_ExtensionReadAhead


__all__ = [
    "SQLite3SpatiaLiteExtension",
    "EmptyPolygon",
    "SQLite3AbstractBase",
    "open",
    "enable_load_extension",
    "SQLite3LibraryError",
    "ope_load_ext",
    "load_ext",
    "default",
]


# -----------------------------------------------------------------------------
# module methods:


_default = None


def default():
    """
    Return the default library-object.

    Return the default library. If no default library is set, a
    SQLite3SpatiaLiteExtension will be created and used as default. The
    default library will be used by all instance of the SQLite3AbstractBase
    class and its children.

    Return
    ------
    : : :class:`~spatialite.SQLite3SpatiaLiteExtension`
        Returns the
