import ctypes
# Test ctypes.CFUNCTYPE

import sys

def callback(arg):
    return arg

CB = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

cb = CB(callback)

assert cb(1) == 1

try:
    cb(1, 2)
except TypeError:
    pass
else:
    print("should raise TypeError")

try:
    cb()
except TypeError:
    pass
else:
    print("should raise TypeError")

# test that ctypes.CFUNCTYPE(None) is allowed

ctypes.CFUNCTYPE(None)(lambda: None)

# test that ctypes.CFUNCTYPE(None)(None) is allowed

