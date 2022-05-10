import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# Test sqlite3.connect(":memory:")
# Test sqlite3.connect("")
# Test sqlite3.connect(None)
# Test sqlite3.connect(":memory:", isolation_level=None)
# Test sqlite3.connect(":memory:", isolation_level="")
# Test sqlite3.connect(":memory:", isolation_level="DEFERRED")
# Test sqlite3.connect(":memory:", isolation_level="IMMEDIATE")
# Test sqlite3.connect(":memory:", isolation_level="EXCLUSIVE")
# Test sqlite3.connect(":memory:", check_same_thread=True)
# Test sqlite3.connect(":memory:", check_same_thread=False)
# Test sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
# Test sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_COLNAMES)
# Test sqlite3.connect(":memory:", factory=None)
#
