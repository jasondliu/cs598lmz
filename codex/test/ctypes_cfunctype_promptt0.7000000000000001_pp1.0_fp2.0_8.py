import ctypes
# Test ctypes.CFUNCTYPE
# XXX is this the right way to do this?
CFUNCTYPE1 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def f(x):
    return x + 42

f1 = CFUNCTYPE1(f)
