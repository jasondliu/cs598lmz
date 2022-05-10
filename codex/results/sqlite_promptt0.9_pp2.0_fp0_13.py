import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() function
sqlite3.connect(":memory:")
# Check the sqlite3 library is aleady loaded.
if ctypes.util.find_library("sqlite3") is None:
    raise ImportError("sqlite3 library not found.")
# Import _sqlite3 from shared object file. 
so = ctypes.CDLL("./libsqlite3.so.0")
# Import _sqlite3 from shared object file. 
so.sqlite3_threadsafe.restype = ctypes.c_int
so.sqlite3_threadsafe.argtypes = None
so.sqlite3_threadsafe()

#print("initial addr: ", hex(id(so._handle)))
#_list, addr = list(), hex(id(so._handle))
#print("librray handle addr: ", addr)
# threadsafe: 0
#print("threadsafe: ", so.sqlite3_threadsafe())
#while True:
#    thread = threading.Thread(target=so.sqlite3_threadsafe(), args=()).start()
#    print(threading
