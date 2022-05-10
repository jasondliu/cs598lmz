import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect('test.db')
# Get a cursor object
cursor = conn.cursor()
# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS script(id INTEGER PRIMARY KEY, thread_id INT, ts DATETIME DEFAULT (datetime('now','localtime')), info TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS thread_info(thread_id INT, update_ts DATETIME DEFAULT (datetime('now','localtime')))''')
conn.commit()
# Insert a row of data
#cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# Save (commit) the changes
#conn.commit()
conn.close()

# This class will be executed in a thread.
class RecordThread(threading.Thread):

    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id
