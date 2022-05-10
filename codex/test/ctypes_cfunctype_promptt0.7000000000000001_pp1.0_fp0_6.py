import ctypes
# Test ctypes.CFUNCTYPE()

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x*x)

if f(9) != 81:
    raise Exception("The result should be 81!")
