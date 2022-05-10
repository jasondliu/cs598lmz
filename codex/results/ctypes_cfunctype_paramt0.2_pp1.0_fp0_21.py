import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    print x
    return x

f = FUNTYPE(func)
f(1)
</code>

