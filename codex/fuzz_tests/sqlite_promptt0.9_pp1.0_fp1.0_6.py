import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:", timeout=2) attempts to do
# ctypes.pythonapi.PyThreadState_SetAsyncExc().
#
# It succeeds in Python 3.2 but will hang on Python 3.2.2.
#
# This difference was fixed by
#   https://hg.python.org/cpython/rev/6ba5b5c5dd5d
#


conn_called = 0
def conn():
    global conn_called
    conn_called += 1
    try:
        con = sqlite3.connect(":memory:", timeout=2)
    except sqlite3.OperationalError:
        pass


th = threading.Thread(target=conn)
th.start()

# Wait for the connection to start.
while conn_called == 0:
    time.sleep(0.1)

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libpthread = ctypes.CDLL(ctypes.util.find_library("pthread"))
th.join(timeout=2)
try:
    assert th
