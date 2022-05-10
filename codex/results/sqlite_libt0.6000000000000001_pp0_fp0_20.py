import ctypes
import ctypes.util
import threading
import sqlite3
import time
import traceback
import os

# Create a mutex.
DECLSPEC_IMPORT = 0x1
MUTEX_ALL_ACCESS = 0x1F0001
g_hMutex = windll.kernel32.CreateMutexA(
    ctypes.c_int(DECLSPEC_IMPORT), 
    ctypes.c_int(0), 
    ctypes.c_char_p("Global\TestMutex"))
if not g_hMutex:
    print "Could not create mutex."
    sys.exit(1)

# Try to acquire the mutex.
dwWaitResult = windll.kernel32.WaitForSingleObject(
    ctypes.c_int(g_hMutex), 
    ctypes.c_int(0))
if dwWaitResult != 0:
    print "Could not acquire mutex."
    sys.exit(1)

# The mutex was acquired.
print "Mutex acquired."

# Do your work...

# Release the mutex.
if not windll.kernel32.
