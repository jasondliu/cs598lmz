import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# See https://www.sqlite.org/c3ref/open.html
# See https://stackoverflow.com/questions/18421757/live-updating-sqlite3-database-from-another-thread

# See https://docs.python.org/3/library/threading.html#threading.Event.wait


# Note that this runs with Python 3.3, 3.4 and 3.5
# but with Python 3.6 the test fails!
# However the test works with Python 2.7, but Python 2 is deprecated.

# Failed attempt to use sqlite3.VFS:
# https://docs.python.org/3/library/sqlite3.html#sqlite3.connect
# https://www.sqlite.org/vfs.html

class VFS(object):
    def __init__(self):
        pass
    def xOpen(self,zVfs,zName,flags,pOutFlags):
        print("VFS xOpen() called")
        return -1

vfs = VFS()
dll =
