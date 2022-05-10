import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

#
# This module is for sharing a sqlite3 database between processes.
#
# The module is based on the following:
#   - https://github.com/benediktschmitt/py-sqlite-shared-cache
#   - https://github.com/benediktschmitt/py-sqlite-shared-cache/blob/master/sqlite_shared_cache/__init__.py
#   - https://www.sqlite.org/sharedcache.html
#
# The following functions are provided:
#
#   - connect(filename, timeout=5.0, isolation_level=None, check_same_thread=True, uri=False, **kwargs):
#       Creates a connection to the database. The connection is shared with
#       other processes.
#
#   - connect_memory(timeout=5.0, isolation_level=None, check_same_thread=True, **kwargs):
#       Creates a connection to a database in memory. The connection is shared
#      
