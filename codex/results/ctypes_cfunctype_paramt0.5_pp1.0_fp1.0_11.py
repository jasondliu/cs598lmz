import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)

def func(x):
    return x**2

fun = FUNTYPE(func)

print(fun(5))
</code>

