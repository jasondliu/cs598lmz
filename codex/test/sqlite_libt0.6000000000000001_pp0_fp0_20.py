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
