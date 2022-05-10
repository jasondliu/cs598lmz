import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/var/mobile/Media/iTunes_Control/iTunes/WordFieldDatabase")

def time_t():
    return int(time.time())

def pp(a):
    if DEBUG:
        #print time.time(), a
        print time.time(), a

def ppp(a,len=60):
    if DEBUG:
        if isinstance(a,unicode):
            #print "\n", time.time(), a.encode("utf-8")
            print a.encode("utf-8")
        else:
            #print "\n", time.time(), a
            print a
            print "-"*len

# iPhone has its own sockets, ctypes_iphone_socket can be used on iOS
# This uses some C code in socketmodule.c
lib = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)
lib.connect.restype = ctypes.c_int
def connect(sock, host, port):
    sa = ctypes.c_int(socket.AF_IN
