import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
SQLITE_LIB_SLN = ctypes.util.find_library('sqlite3')
SQLITE_LIB_DLL = r'E:\Projects\dll2py\sqlite-dll-win32-x86-3230100\sqlite3.dll'
SQLITE_LIB_DLL_WIN32_VC6 = r'E:\Projects\dll2py\sqlite-dll-win32-x86-3230100\sqlite-vc6-8987150\sqlite3.dll'
SQLITE_LIB_DLL_WIN32_VC7 = r'E:\Projects\dll2py\sqlite-dll-win32-x86-3230100\sqlite-vc7-8750000\sqlite3.dll'
SQLITE_LIB = SQLITE_LIB_DLL_WIN32_VC6
