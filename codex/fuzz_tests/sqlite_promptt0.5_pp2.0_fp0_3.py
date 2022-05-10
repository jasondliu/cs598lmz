import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect

# import sqlite3
# con = sqlite3.connect('test.db')
# with con:
#     cur = con.cursor()
#     cur.execute("CREATE TABLE IF NOT EXISTS Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
#     cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
#     cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
#     cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
#     cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")
#     cur.execute("INSERT INTO Friends(Name) VALUES ('Julian');")
#     cur.execute("INSERT INTO Friends(Name) VALUES ('Sandra');")
#     cur.execute("INSERT INTO Friends(Name) VALUES ('Kristin');")
#     cur.execute("INSERT INTO Friends(Name) VALUES ('Adam');")
#     cur.execute("INSERT INTO Friends(Name) VALUES ('Jenny');")
#     cur
