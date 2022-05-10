import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect or sqlite3.Connection
import sqlite3 as testmod


# NOTE: This test is designed to be run from the sqlite3/test directory.
# It assumes that the "dbapi20.py" and "dbapi20_tpc.py" files are in the
# same directory as this file.

# Get the module, assuming we're in the test directory.
dbapi20 = imp.load_source('dbapi20', 'dbapi20.py')
dbapi20_tpc = imp.load_source('dbapi20_tpc', 'dbapi20_tpc.py')

# Some of the SQL we'll need.

defs = {
    'paramstyle': 'named',
    'threadsafety': 1,
    'apilevel': '2.0',
    'paramstyle': 'named',
    'threadsafety': 1,
    'get_info': {
        'server_version': '3.6.23',
        'sqlite_version': '3.6.23',
        'database_name': 'main',
        'proto_
