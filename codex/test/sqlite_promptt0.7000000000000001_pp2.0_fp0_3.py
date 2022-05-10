import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')
import time

# Setting up the db
conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_data( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_data INTEGER \
        )")
    conn.commit()
conn.close()

# Start defining the functions for the callback
def callback_func(data):
    print('Callback called with data = %d' % data)

def py_error_handler(filename, line, function, err, fmt):
    pass

# Set the error handler so that we can ignore the errors for now
ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

