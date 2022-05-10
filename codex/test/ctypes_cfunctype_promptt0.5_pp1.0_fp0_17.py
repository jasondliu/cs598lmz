import ctypes
# Test ctypes.CFUNCTYPE()
def func(a, b):
    print("func() called with %d and %d" % (a, b))

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmpptr = CMPFUNC(func)
