import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('/home/jeff/.config/google-chrome/Default/History')
c = conn.cursor()
c.execute('''SELECT * FROM urls''')

print c.fetchone()

conn.close()
