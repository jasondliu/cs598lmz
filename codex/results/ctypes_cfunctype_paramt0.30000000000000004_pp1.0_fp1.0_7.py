import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def c_func(x):
    return x**2

c_func_ptr = FUNTYPE(c_func)

def func(x):
    return c_func_ptr(x)

print(func(2))
</code>

