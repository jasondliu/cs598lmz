import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# conn = sqlite3.connect("test.db")
# c = conn.cursor()
# c.execute("CREATE TABLE test(id int, name text)")
# c.execute("INSERT INTO test (id, name) VALUES (1, 'This is test')")
# c.execute("INSERT INTO test (id, name) VALUES (2, 'This is test2')")
# c.execute("INSERT INTO test (id, name) VALUES (3, 'This is test3')")
# c.execute("INSERT INTO test (id, name) VALUES (4, 'This is test4')")
# conn.commit()
# c.execute("SELECT * FROM test")
# for row in c:
#     print(row)

# Test sqlite3.connect() using with
with sqlite3.connect("test.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test")
    print(cursor.fetchall())

# Test ctypes.util.find_library()
