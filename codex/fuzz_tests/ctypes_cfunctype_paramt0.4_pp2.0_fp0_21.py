import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def my_func(x):
    return x*x

c_func = FUNTYPE(my_func)

print c_func(2.0)
</code>

