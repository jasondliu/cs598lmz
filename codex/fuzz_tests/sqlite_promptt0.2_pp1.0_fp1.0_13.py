import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

# This is a simple example of a ctypes wrapper for a C library.
# The library is libm, the standard C math library.

# The ctypes.cdll.LoadLibrary function takes a string containing the
# name of the library to load.  On Windows, this string can be either
# an absolute pathname, or a filename in the current directory, or a
# filename in the directory where the DLL search path points.  On
# Unix, the string must be an absolute pathname.

# libm = ctypes.cdll.LoadLibrary('libm.so')
# libm = ctypes.cdll.LoadLibrary('libm.dylib')
# libm = ctypes.cdll.LoadLibrary('libm.dll')

# The ctypes.util.find_library function takes a library name, and
# returns a string containing the absolute pathname.

libm = ctypes.cdll.LoadLibrary(ctypes.util.find_library('m'))

# The math library functions are declared as extern functions in
# header files.  The declarations
