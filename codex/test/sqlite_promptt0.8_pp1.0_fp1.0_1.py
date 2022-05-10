import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file::memory:?cache=shared')
# Do sqlite3.enable_shared_cache(True) AFTER opening shared connections

