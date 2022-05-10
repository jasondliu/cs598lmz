import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

func = FUNTYPE(f)
print func(5)

func = FUNTYPE(lambda x: x**3)
print func(5)
</code>

