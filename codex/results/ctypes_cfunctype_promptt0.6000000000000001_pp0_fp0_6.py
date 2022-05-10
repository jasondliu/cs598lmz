import ctypes
# Test ctypes.CFUNCTYPE.

ctypes.CFUNCTYPE

def callback(arg):
    return arg

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

CALLBACK(callback)
