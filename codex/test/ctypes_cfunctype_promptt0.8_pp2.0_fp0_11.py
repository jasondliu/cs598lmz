import ctypes
# Test ctypes.CFUNCTYPE by creating a ctypedef c_int(c_int) function pointer 
# type, and setting it to the same address as inc, below.
functype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
