import ctypes
# Test ctypes.CFUNCTYPE
# ctypes.CFUNCTYPE(<restype>, <argtypes>)
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def Add(a, b):
    return a + b

Add(1, 2)
# 3

