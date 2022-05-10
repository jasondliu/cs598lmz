import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()'s lru cache.
#
# The problem: sqlite3 module uses a global LRU cache for the
# sqlite3.connect() call. This means that the Python interpreter won't be
# able to exit cleanly if the cache contains references to ZipFile objects.
#
# Solution: Make sure that ZipFile objects aren't placed in the cache
# (preferably by not using sqlite3!), or empty the cache manually.
#
# Notes:
#  - The sqlite3 module is compiled in - so this problem is only relevant
#    if the module is actually used
#  - The problem is not fixed in Python 3.2.2, maybe it was fixed in 3.3
#  - The fix_atexit_issue.py module makes sure that the problem doesn't
#    cause the Python interpreter to hang.
import collections
try:
    from . import pure

    def test_zipfile_from_buffer():
        pure.py_zipfile_from_buffer(b'', lambda: b'')
except ImportError:
    def test_zipfile_from_buffer():
        pass

