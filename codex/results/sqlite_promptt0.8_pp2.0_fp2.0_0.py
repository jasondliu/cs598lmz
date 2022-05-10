import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:', uri=True)
try:
    import sqlitebck
except ImportError:
    sqlitebck = None

#
# Some tests rely on the ability to create a large number of
# simultaneous connections to SQLite.  This is only possible
# if SQLite is compiled with the SQLITE_THREADSAFE pre-processor
# macro set to 1.  Python is normally compiled with threadsafe=1
# so it is only necessary to recompile SQLite itself.
#
# The sqlite.test() function will raise an exception if it
# determines that the library is not threadsafe.
#

sqlite_version_info = (3, 6, 22, 1)
sqlite_version = '.'.join(str(x) for x in sqlite_version_info)
if sqlite_version_info < (3, 3, 1):
    raise Exception("SQLite 3.3.1 or newer is required")

if sqlite_version_info < (3, 3, 4):
    have_threadsafe = 0
else:
    have_threadsafe =
