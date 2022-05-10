import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def square(x):
    return x*x

func = FUNTYPE(square)
print func(2)
</code>

