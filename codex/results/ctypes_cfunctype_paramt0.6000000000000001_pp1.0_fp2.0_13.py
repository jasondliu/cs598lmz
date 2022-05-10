import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_float)

def fun(x):
    return x**2

f = FUNTYPE(fun)

print(f(2))
</code>

