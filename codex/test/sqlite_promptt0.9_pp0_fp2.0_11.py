import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)
#
# Also see https://bitbucket.org/ogrisel/sharedcache/src/b101d0751d70/
# sharedcache/__init__.py?at=default

