import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def callback(x, y):
    return x + y

cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(callback)
