import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() works
path = sqlite3.connect("/Users/dbarkema/Desktop/tv.sqlite")
cursor = sqlite3.Cursor
conn = sqlite3.connect("/Users/dbarkema/Desktop/tv.sqlite")
c = conn.cursor()
try:
    c.execute('''CREATE TABLE channels
                 (name text, channels text)''')
except:
    pass
try:
    c.execute('''INSERT INTO channels 
               VALUES ('channels', 'A B C')''')
except:
    pass

try:
    c.execute('''CREATE TABLE shows
                 (name text, channels text, start text, end text)''')
except:
    pass
try:
    c.execute('''INSERT INTO shows 
               VALUES ('show', 'a b c','12:00','12:30')''')
except:
    pass
conn.commit()
conn.close()
conn = sqlite3.connect("/Users/dbarkema/Desktop/tv.sqlite")
