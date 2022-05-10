import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
import time

# This is the function we want to call from the shared library
# The argtypes and restype must be set, or ctypes will fail
# to call the function.
#
# The argtypes are the C data types of the arguments, and
# restype is the C data type of the return value.
#
# In this case, the function takes no arguments and returns
# nothing.
_test = None
_test.argtypes = []
_test.restype = None

# This is the function we want to call from the shared library
# The argtypes and restype must be set, or ctypes will fail
# to call the function.
#
# The argtypes are the C data types of the arguments, and
# restype is the C data type of the return value.
#
# In this case, the function takes no arguments and returns
# nothing.
_test1 = None
_test1.argtypes = []
_test1.restype = None

# This is the function we want to call from the shared library
# The argtypes and restype must be set, or
