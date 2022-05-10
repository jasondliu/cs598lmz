import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

# This is the library we are going to load.
# The name is platform dependent.
libname = ctypes.util.find_library("c")
if not libname:
    raise Exception("Can't find C library")

# Load the library into ctypes
lib = ctypes.CDLL(libname)

# This is the prototype of the function we are going to call.
# The parameters must be ctypes types.
lib.printf.restype = ctypes.c_int
lib.printf.argtypes = [ctypes.c_char_p]

# Now we can call the function.
lib.printf("Hello world\n")

# We can also call printf from Python.
# This is the same as lib.printf("Hello world\n")
ctypes.pythonapi.PyFile_AsFile.restype = ctypes.c_void_p
ctypes.pythonapi.PyFile_AsFile.argtypes = [ctypes.py_object]
fp = ctypes.pythonapi.PyFile_AsFile(ctypes.sys.stdout)
