import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)
#
# Also see https://bitbucket.org/ogrisel/sharedcache/src/b101d0751d70/
# sharedcache/__init__.py?at=default

try:
    sqlite3.enable_shared_cache(True)
except:
    print 'Cannot enab
