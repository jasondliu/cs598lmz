import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def myfunc(x):
    return x**2

f = FUNTYPE(myfunc)
print(f(2))
</code>

