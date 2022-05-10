import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/home/szymek/Desktop/test.db')

# Create database if it doesn't exist
# conn = sqlite3.connect('/home/szymek/Desktop/test.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS [Test] ([id] INTEGER PRIMARY KEY AUTOINCREMENT, [date] DATETIME, [value] REAL);''')
# conn.commit()
# conn.close()

# Create a mutex
mutex = threading.Lock()

# Create a new ttyUSB port
def create_new_port():
	# Search for ttyUSB ports
	for i in range(0, 10):
		port = '/dev/ttyUSB' + str(i)
