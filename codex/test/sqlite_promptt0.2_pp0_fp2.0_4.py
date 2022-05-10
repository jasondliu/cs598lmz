import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# Test sqlite3.connect(":memory:")
# Test sqlite3.connect(":memory:", check_same_thread=False)
# Test sqlite3.connect(":memory:", check_same_thread=True)
# Test sqlite3.connect(":memory:", check_same_thread=False, isolation_level=None)
# Test sqlite3.connect(":memory:", check_same_thread=False, isolation_level="")
# Test sqlite3.connect(":memory:", check_same_thread=False, isolation_level="DEFERRED")
# Test sqlite3.connect(":memory:", check_same_thread=False, isolation_level="IMMEDIATE")
# Test sqlite3.connect(":memory:", check_same_thread=False, isolation_level="EXCLUSIVE")
# Test sqlite3.connect(":memory:", check_same_thread=False, isolation_level="DEFERRED", uri=True)
# Test sqlite3.connect(":memory:", check_same_thread=False, isolation_level
