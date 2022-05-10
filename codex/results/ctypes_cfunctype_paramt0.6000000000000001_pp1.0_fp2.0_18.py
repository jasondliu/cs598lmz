import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)

def f(x):
    return x

func = FUNTYPE(f)

print func(1)
</code>

