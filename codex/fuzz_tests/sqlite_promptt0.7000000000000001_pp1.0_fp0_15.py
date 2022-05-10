import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
N = 10

threads = [
    threading.Thread(
        target = lambda: sqlite3.connect(":memory:"))
    for i in range(N)
]

for t in threads:
    t.start()

for t in threads:
    t.join()
import sys
sys.version_info

import sqlite3

sqlite3.sqlite_version

 
# Open database connection
db = sqlite3.connect("mydb.db")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % data)

# disconnect from server
db.close()
import sqlite3

connection = sqlite3.connect("mydb.db")

crsr = connection.cursor() 

sql_command = """CREATE TABLE employee ( 
