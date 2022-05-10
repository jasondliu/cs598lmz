import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect's timeout arg
import time

libedit = ctypes.cdll.LoadLibrary(ctypes.util.find_library('edit'))
libedit.el_init(0, 0, 0)
line = ctypes.create_string_buffer(32)
hist = libedit.history_init()
libedit.history(hist, ctypes.byref(line), libedit.H_ENTER, 'To be or not to be.\0')
libedit.history(hist, ctypes.byref(line), libedit.H_ENTER, 'What is it?\0')

# test EOF and SIGINT handling
for _ in range(10):
    libedit.read_history(hist, None)
    libedit.read_history(hist, None)
    libedit.read_history(hist, None)
    libedit.read_history(hist, None)

if threading.active_count() < 3:
    print(threading.active_count())
    raise RuntimeError

