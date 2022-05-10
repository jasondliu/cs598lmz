import ctypes
import ctypes.util
import threading
import sqlite3
import find_libs_by_extension


def guess_sqlite_lib():
    # Add some hooks for the SQLite module.
    lib = ctypes.util.find_library('sqlite3')
    if not lib:
        # Guess and use one of the libsqlite* libraries in the system.
        lib = find_libs_by_extension.find_libs_by_extension('.so', 'libsqlite')
        if not lib:
            raise Exception('No SQLite library found')
        lib = lib[0]
    return lib

class SqliteStatement(object):

    def __init__(self, stmt, sql_stmt, db):
        self._stmt = stmt
        self._sql_stmt = sql_stmt
        self._db = db
        self._owning_db = None
        self._owning_connection = None


    @property
    def sql(self):
        return self._sql_stmt

   
    def bind(self, *args):
        sqlite3.sqlite3
