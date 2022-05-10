import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/tmp/test.db")

class C(ctypes.Structure):
    _fields_ = [("i", ctypes.c_int)]

def callback(user_data, cols, values, names):
    print("callback called")
    print("user_data=%s" % user_data)
    print("cols=%s" % cols)
    print("values=%s" % values)
    print("names=%s" % names)

def callback2(user_data, cols, values, names):
    print("callback2 called")
    print("user_data=%s" % user_data)
    print("cols=%s" % cols)
    print("values=%s" % values)
    print("names=%s" % names)

def callback3(user_data, cols, values, names):
    print("callback3 called")
    print("user_data=%s" % user_data)
    print("cols=%s" % cols)
    print("values=%s
