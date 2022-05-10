import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')
# Test sqlite3.connect('file:/dev/shm/python-sqlite3-ctypes?')

### Read sqlite3.h, sqlite3ext.h, sqlite3.c

### Exceptions

# Not specified exactly in the documentation, but in
# Modules/_sqlite/cursor.c:
class DatabaseError(Exception):
    pass

class ProgrammingError(DatabaseError):
    pass

class Warning(Exception):
    pass

class InterfaceError(DatabaseError):
    pass

class OperationalError(DatabaseError):
    pass

class IntegrityError(DatabaseError):
    pass

class InternalError(DatabaseError):
    pass

class NotSupportedError(DatabaseError):
    pass

### Type Objects
class SQLiteTypeObject(object):
    """Type object for exported objects"""
    py_type = None
    sqlite_type = None

    @classmethod
    def __getitem__(cls, py_type):
        if not cls.py_type:
            cls
