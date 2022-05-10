import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
sqlite3.connect(':memory:')
#dl = ctypes.CDLL(ctypes.util.find_library('sqlite3'))
#ctypes.pythonapi.PyThreadState_SetAsyncExc.argtypes = [ctypes.c_long, ctypes.py_object]
#ctypes.pythonapi.PyThreadState_SetAsyncExc.restype = ctypes.c_int
#def kill_thread(thread):
#    assert thread.isAlive(), "thread must be started"
#    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
#        ctypes.c_long(thread.ident), ctypes.py_object(SystemExit))
#    if res == 0:
#        raise ValueError("invalid thread id")
#    elif res != 1:
#       # """if it returns a number greater than one, you're in trouble,
#       # and you should call it again with exc=NULL to revert the effect"""
#        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
#       
