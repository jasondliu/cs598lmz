import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect 

sqlite3.connect("test.db")

# connect to database
db = sqlite3.connect("test.db")
cursor = db.cursor()

# create table
cursor.execute("""CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)""")
db.commit()

# insert data
cursor.execute("""INSERT INTO test (name) VALUES ('test')""")
cursor.execute("""INSERT INTO test (name) VALUES ('test2')""")
db.commit()

# read data
for row in cursor.execute("SELECT * FROM test"):
    print(row)

db.close()
# import ctypes
# import ctypes.util
# import threading
# import sqlite3
# import time

# def test_thread():
#     print("start thread")
#     time.sleep(1)
#     print("end thread")

# # First find the library
# if ctypes.util.find_library('libsqlite3
