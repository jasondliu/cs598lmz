import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

c_f = FUNTYPE(f)

print c_f(2)
</code>

