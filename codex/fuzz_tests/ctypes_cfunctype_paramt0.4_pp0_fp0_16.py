import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x*x

def func2(x):
    return x*x*x

f = FUNTYPE(func)
f2 = FUNTYPE(func2)

print f(2)
print f2(2)
</code>

