import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# conn = sqlite3.connect('log/mydatabase.db')
# print "Opened database successfully";
# conn.close()

# create thread for epe_callback()
epe_thread = threading.Thread(target=epe_callback)

# start epe_thread
epe_thread.start()

# initialize EPE
epe_initialize()

# open serial port
