import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
try:
    sqlite3.connect(':memory:')
    sqlite3.connect(':memory:', check_same_thread=False)
except sqlite3.ProgrammingError: pass
else:
    print('sqlite3.connect() did not require an argument with check_same_thread=False')
    assert False

try: conn = sqlite3.connect(':memory:', check_same_thread=True)
except sqlite3.ProgrammingError: pass
else:
    print('sqlite3.connect() rejected an argument with check_same_thread=True')
    assert False

# Test sqlite3.Connection.__del__()
try:
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    assert prop(conn, '_is_thread_sharing_conn') is True
except:
    pass
else:
    del conn

# Test sqlite3.Connection.__enter__()
