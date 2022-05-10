import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

from . import _sqlite3

class Error(Exception):
    pass

class Warning(Exception):
    pass

class InterfaceError(Error):
    pass

class DatabaseError(Error):
    pass

class InternalError(DatabaseError):
    pass

class OperationalError(DatabaseError):
    pass

class ProgrammingError(DatabaseError):
    pass

class IntegrityError(DatabaseError):
    pass

class DataError(DatabaseError):
    pass

class NotSupportedError(DatabaseError):
    pass

def _check_remaining_sql(remaining):
    if remaining:
        raise Warning("You can only execute one statement at a time.")

def _check_sqlite_ok(error):
    if error:
        raise sqlite3.OperationalError(error)

def _check_sqlite_error(error):
    if error:
        raise sqlite3.DatabaseError(error)

