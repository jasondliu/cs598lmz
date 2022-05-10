import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
try:
    sqlite3.connect(':memory:')
except Exception as e:
    print('Cannot connect to sqlite3 database')
    print(e)
    sys.exit(1)

#------------------------------------------------------------------------------
# Find and load the library
#------------------------------------------------------------------------------

lib = ctypes.util.find_library('libpython2.7.so')
if not lib:
    print('Cannot find libpython2.7.so')
    sys.exit(1)
lib = ctypes.cdll.LoadLibrary(lib)

#------------------------------------------------------------------------------
# Patch the library
#------------------------------------------------------------------------------

# PyEval_ReleaseLock
def PyEval_ReleaseLock():
    lib.PyEval_AcquireLock()
    lib.PyEval_ReleaseLock()
    lib.PyEval_ReleaseLock()
    return
lib.PyEval_ReleaseLock = PyEval_ReleaseLock

# PyGILState_Ensure
def PyGILState_Ensure():
    lib.PyEval_AcquireLock()
    return 0
lib.PyGIL
