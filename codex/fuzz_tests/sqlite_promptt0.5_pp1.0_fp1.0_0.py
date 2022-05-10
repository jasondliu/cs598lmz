import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

#conn = sqlite3.connect('example.db')

#c = conn.cursor()

# Create table
#c.execute('''CREATE TABLE stocks
#             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
#conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#conn.close()

def get_dblib_path():
    if sys.platform == 'darwin':
        return ctypes.util.find_library('libsqlite3.dylib')
    elif sys.platform == 'win32':
        return ctypes.util.find_library('sqlite3')
    else:
        return ctypes.util.find_library('sqlite3')

class SQLite3(object
