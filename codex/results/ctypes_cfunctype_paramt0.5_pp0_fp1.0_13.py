import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def wrapper(f):
    return FUNTYPE(f)

@wrapper
def f(x, y):
    return x + y

print f(1.0, 2.0)
</code>

