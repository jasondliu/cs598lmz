import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect with timeout.
# This test needs a connection to a database that takes longer than
# the timeout to connect.
try:
    conn = sqlite3.connect(":memory:", timeout=0.1)
    conn.close()
except sqlite3.OperationalError as e:
    print("Failed to connect to :memory:")
    print(e)
    raise SystemExit

# Test sqlite3.connect with timeout and isolation_level.
try:
    conn = sqlite3.connect(":memory:", timeout=0.1, isolation_level='DEFERRED')
    conn.close()
except sqlite3.OperationalError as e:
    print("Failed to connect to :memory:")
    print(e)
    raise SystemExit

# Test sqlite3.connect with timeout and uri.
try:
    conn = sqlite3.connect("file:memory:?cache=shared", timeout=0.1)
    conn.close()
except sqlite3.OperationalError as e:
    print("Failed to connect to file:memory:?cache=
