import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memdb1?mode=memory&cache=shared', uri=True)
# Test sqlite3.connect('file:memdb1?mode=memory', uri=True)
# Test sqlite3.connect('file:memdb1?cache=shared', uri=True)

# Test sqlite3.connect('file:memdb2?mode=memory&cache=shared', uri=True)
# Test sqlite3.connect('file:memdb2?mode=memory', uri=True)
# Test sqlite3.connect('file:memdb2?cache=shared', uri=True)

sqlite_version = sqlite3.sqlite_version_info
sqlite_version_string = sqlite3.sqlite_version

def print_sqlite_version():
    print('sqlite3', sqlite_version_string)

def print_pysqlite_version():
    print('pysqlite', sqlite3.version)

def print_python_version():
    print('python', sys.version)

def create_connection
