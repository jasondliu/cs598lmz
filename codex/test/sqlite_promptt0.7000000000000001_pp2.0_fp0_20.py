import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:').execute('select 1').fetchone()
from ctypes import c_int, c_char_p, c_void_p, pointer, cast, POINTER, Structure, CFUNCTYPE
from ctypes.util import find_library


def find_sqlite_lib():
    library_name = find_library('sqlite3')
    if library_name is None:
        library_name = find_library('libsqlite3')
    if library_name is None:
        raise ImportError('No suitable sqlite3 library found')
    return library_name


class SQLite3Error(sqlite3.OperationalError):
    """Exception raised for errors that are related to the database"""
    pass


class SQLite3Warning(sqlite3.Warning):
    """Exception raised for errors that are related to the database"""
    pass


class SQLite3InterfaceError(sqlite3.InterfaceError):
    """Exception raised for errors that are related to the database"""
    pass


