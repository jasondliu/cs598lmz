import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x

f = FUNTYPE(func)
print(f(1))
</code>

