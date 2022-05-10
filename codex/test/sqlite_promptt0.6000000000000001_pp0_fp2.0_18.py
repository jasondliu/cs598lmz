import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/tmp/test.db")
# Test sqlite3.connect("/tmp/test.db", check_same_thread=False)
# Test sqlite3.connect("/tmp/test.db", detect_types=sqlite3.PARSE_DECLTYPES)
# Test sqlite3.connect("/tmp/test.db", detect_types=sqlite3.PARSE_COLNAMES)
# Test sqlite3.connect("/tmp/test.db", factory=MyConnection)
# Test sqlite3.connect("/tmp/test.db", timeout=1000)
# Test sqlite3.connect("/tmp/test.db", isolation_level=None)
# Test sqlite3.connect("/tmp/test.db", isolation_level="DEFERRED")
# Test sqlite3.connect("/tmp/test.db", isolation_level="IMMEDIATE")
# Test sqlite3.connect("/tmp/test.db", isolation_level="EXCLUSIVE")
# Test sqlite3.connect("/tmp/test.db", detect_types=sqlite3
