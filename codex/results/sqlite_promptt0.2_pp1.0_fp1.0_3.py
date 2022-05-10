import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
#conn = sqlite3.connect('/home/pi/Desktop/test.db')
#print "Opened database successfully";
#conn.close()

# Test ctypes.util.find_library()
#libc = ctypes.util.find_library('c')
#print libc

# Test ctypes.CDLL()
#libc = ctypes.CDLL(libc)
#print libc

# Test ctypes.CDLL().time()
#print libc.time(None)

# Test ctypes.CDLL().localtime()
#t = libc.time(None)
#print t
#print ctypes.cast(t, ctypes.POINTER(ctypes.c_int)).contents.value
#print ctypes.cast(libc.localtime(t), ctypes.POINTER(ctypes.c_int)).contents.value

# Test ctypes.CDLL().localtime()
#print ctypes.cast(libc.localtime(libc.time(None)), ctypes.POINTER(ctypes.c_
