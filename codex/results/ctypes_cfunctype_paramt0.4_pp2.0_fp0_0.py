import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def f(x):
    return x+1

func = FUNTYPE(f)

print func(1)
</code>

