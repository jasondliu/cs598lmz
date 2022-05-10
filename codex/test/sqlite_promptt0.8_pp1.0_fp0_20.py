import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("my_database").execute("PRAGMA synchronous = OFF;")


libpython_path = ctypes.util.find_library("python3.3m")
print("libpython_path: " + str(libpython_path))
libpython = ctypes.CDLL(libpython_path)

print("libpython: " + str(libpython))

#  No need to call Py_Initialize()/Py_Finalize()
libpython.PyEval_InitThreads()
print("libpython.PyEval_InitThreads: " + str(libpython.PyEval_InitThreads))

my_thread_state = libpython.PyEval_SaveThread()
print("my_thread_state: " + str(my_thread_state))

#
# # Do some work
#

# libpython.PyEval_RestoreThread(my_thread_state)
# libpython.Py_Finalize()


# my_thread_state = libpython.PyEval_SaveThread()
# print("my_thread_state: " + str(
