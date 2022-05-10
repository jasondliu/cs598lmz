import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.c_uint, ctypes.c_uint)
def func(x, y):
    return x + y

myfunc = FUNTYPE(func)
print myfunc(2, 3)
</code>

