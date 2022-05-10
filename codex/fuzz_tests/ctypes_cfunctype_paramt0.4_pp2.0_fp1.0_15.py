import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

def g(x):
    return x**3

fptr = FUNTYPE(f)
gptr = FUNTYPE(g)

print(fptr(2))
print(gptr(2))
</code>

