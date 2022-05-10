import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

# Create a new database in memory
con = sqlite3.connect(':memory:')

# Create a new cursor
cur = con.cursor()

# Execute a statement to create a new table
cur.execute("CREATE TABLE IF NOT EXISTS todo(id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")

# Execute a statement to insert two rows into the new table
cur.execute("INSERT INTO todo(task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
cur.execute("INSERT INTO todo(task,status) VALUES ('Visit the Python website',1)")
cur.execute("INSERT INTO todo(task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
cur.execute("INSERT INTO todo(task,status) VALUES ('Choose your favorite WSGI-Framework',0)")

# Execute a statement to select all rows from the table
cur.execute("SELECT id,task
