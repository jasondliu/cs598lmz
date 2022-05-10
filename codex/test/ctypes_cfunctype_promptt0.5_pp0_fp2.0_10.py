import ctypes
# Test ctypes.CFUNCTYPE()
def foo(x, y):
    return x + y

f = ctypes.CFUNCTYPE(ctypes.c_int)(foo)
