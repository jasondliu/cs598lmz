import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# Test sqlite3.cursor
# Test sqlite3.Column
# Test sqlite3.Row
# Test sqlite3.Connection
# Test sqlite3.Cursor
# Test sqlite3.Row
# Test sqlite3.connections
# Test sqlite3.threadsafety
# Test sqlite3.paramstyle
# Test sqlite3.complete_statement
# Test sqlite3.version
# Test sqlite3.sqlite_version
# Test sqlite3.sqlite_version_info
# Test sqlite3.sqlite_encoding
# Test sqlite3.sqlite_source_id
# Test sqlite3.sqlite_compileoption_get
# Test sqlite3.sqlite_compileoption_used
# Test sqlite3.thread_cleanup

def _is_64bit():
    return sys.maxsize > 2**32

def _is_pysqlite_raw():
    return 'pysqlite_raw' in sys.modules

def _is_pysqlite_native():
    return 'pysqlite_
