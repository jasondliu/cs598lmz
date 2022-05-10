import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("data.db")
# Test sqlite3.connect("data.db", check_same_thread=False)
# Test sqlite3.connect("data.db", detect_types=sqlite3.PARSE_DECLTYPES)
# Test sqlite3.connect("data.db", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
# Test sqlite3.connect("data.db", factory=MyConnection)
# Test sqlite3.connect("data.db", detect_types=sqlite3.PARSE_DECLTYPES, factory=MyConnection)
# Test sqlite3.connect("data.db", timeout=10.0)
# Test sqlite3.connect("data.db", timeout=10.0, isolation_level=None)
# Test sqlite3.connect("data.db", timeout=10.0, isolation_level="DEFERRED")
# Test sqlite3.connect("data.db", timeout=10.0, isolation_level="IMMEDIATE")
# Test sqlite3
