import ctypes
# Test ctypes.CFUNCTYPE

# This should work

libc = ctypes.CDLL(None)

def callback(x, y):
    return x + y

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cb = CALLBACK(callback)

assert cb(1, 2) == 3

# This should raise an exception

try:
    CALLBACK(5)
except TypeError:
    pass
else:
    print("Expected TypeError")
