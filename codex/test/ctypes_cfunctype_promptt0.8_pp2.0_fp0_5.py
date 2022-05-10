import ctypes
# Test ctypes.CFUNCTYPE()
def func(x): return x + 1
pf = ctypes.CFUNCTYPE(ctypes.c_int)(func)
