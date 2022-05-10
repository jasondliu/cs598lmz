import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_func(f):
    return FUNTYPE(f)

def f(x):
    return x**2

g = make_func(f)
print g(2)
</code>

