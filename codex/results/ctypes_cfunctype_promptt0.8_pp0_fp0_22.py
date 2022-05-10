import ctypes
# Test ctypes.CFUNCTYPE for use as callbacks in Cython
#
# The C code comes from the Python documentation:
#   https://docs.python.org/3.5/library/ctypes.html#callback-functions
#
# But the 'example callbacks.py' file does not work as is.
#
# This is the complete version:
#
#   import ctypes
#   import sys
#
#   # This is the prototype of the callback function:
#   CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p)
#
#   def py_callback(a, b, c):
#       # This function will be called instead of the C function
#       print("The callback function was called with parameters " + str(a) + ", " + str(b) + ", " + str(c))
#       return a + b - c
#
#   # The C callback is defined in C and named "callback"
#   callback = CALLBACK(py_callback)
#
