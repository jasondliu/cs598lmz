import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')
import sqlite3
db = sqlite3.connect('test.db')
dbcursor = db.cursor()
dbcursor.execute('''SELECT * FROM Students''')

for row in dbcursor:
    print row
