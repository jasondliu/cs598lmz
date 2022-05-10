import ctypes
# Test ctypes.CFUNCTYPE
def func(arg):
    print("func() called with arg =", arg)

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

cmpproc = CMPFUNC(func)
cmpproc(42)
