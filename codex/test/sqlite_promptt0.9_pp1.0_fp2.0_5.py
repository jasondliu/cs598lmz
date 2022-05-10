import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect sync

# os.environ['SQLITE_ASYNC_THREADS'] = '1'

conn = sqlite3.connect("foo.db")
cursor = conn.cursor()
cursor.execute("select * from x")
print("If this prints, the sync bug is not present")
cursor.fetchall()
