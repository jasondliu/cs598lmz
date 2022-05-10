import ctypes
# Test ctypes.CFUNCTYPE by creating a function that calls back to
# Python.  This is a rather contrived example, but it is effective.

callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

