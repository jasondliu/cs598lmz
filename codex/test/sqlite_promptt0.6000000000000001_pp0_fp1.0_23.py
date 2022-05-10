import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#conn = sqlite3.connect("test.db")
#c = conn.cursor()
#c.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, value INTEGER)")
#c.execute("INSERT INTO test (value) VALUES (42)")
#conn.commit()
#c.execute("SELECT * FROM test")
#print(c.fetchone())
#conn.close()

# Test sqlite3.Row
#conn = sqlite3.connect("test.db")
#conn.row_factory = sqlite3.Row
#c = conn.cursor()
#c.execute("SELECT * FROM test")
#print(c.fetchone()["value"])
#conn.close()


# Test sqlite3.Row with multiple columns
#conn = sqlite3.connect("test.db")
#conn.row_factory = sqlite3.Row
#c = conn.cursor()
#c.execute("SELECT * FROM test")
#row = c.fetchone()
#
