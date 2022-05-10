import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def fun(x):
    return x**2

f = FUNTYPE(fun)

print(f(3))

def fun2(x):
    return x*2

f2 = FUNTYPE(fun2)

print(f2(3))
</code>

