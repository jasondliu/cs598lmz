import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(a):
    return a*a

cfunc = FUNTYPE(func)

lib = ctypes.CDLL("./libtest.so")
lib.call_func(cfunc)
