import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

s = sqlite3.connect("test_db")
c = s.cursor()

c.execute("select count(*) from sqlite_master where type='table';")
print("sqlite_master table size: {0}".format(c.fetchone()))

for row in c.execute("select * from sqlite_master;"):
    print(row)

c.close()
