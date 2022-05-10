import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
#conn = sqlite3.connect('test.db')
#print "Opened database successfully";

# Test ctypes
#libc = ctypes.CDLL(ctypes.util.find_library('c'))
#print 'Calling libc.getpid()'
#print 'PID:', libc.getpid()

# Test threading
#def worker():
#    print 'Worker'
#    return
#
#threads = []
#for i in range(5):
#    t = threading.Thread(target=worker)
#    threads.append(t)
#    t.start()

# Test ctypes.util.find_library()
#print ctypes.util.find_library('c')
#print ctypes.util.find_library('m')
#print ctypes.util.find_library('pthread')
#print ctypes.util.find_library('dl')
#print ctypes.util.find_library('util')
#print ctypes.util.find_library('nsl')
#print ctypes.util
