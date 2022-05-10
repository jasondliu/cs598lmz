import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() and sqlite3.connect().cursor()

print("sqlite3.connect()")
con = sqlite3.connect(":memory:")
con.close()

print("sqlite3.connect().cursor()")
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.close()
con.close()

# Test sqlite3.connect() with isolation_level
print("sqlite3.connect() with isolation_level")
con = sqlite3.connect(":memory:", isolation_level="EXCLUSIVE")
con.close()
con = sqlite3.connect(":memory:", isolation_level="IMMEDIATE")
con.close()
con = sqlite3.connect(":memory:", isolation_level="DEFERRED")
con.close()

# Test sqlite3.connect() with detect_types
print("sqlite3.connect() with detect_types")
con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_COLNAMES)
con.close()
con
