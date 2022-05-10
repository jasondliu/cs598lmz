import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)
def f(i):
    print i

funchandler = FUNTYPE(f)
