import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def my_func(x):
    return x**2

f = FUNTYPE(my_func)
print f(2)
</code>

