import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)
def func(x):
    return x*2

myfunc = FUNTYPE(func)

print myfunc(5)
