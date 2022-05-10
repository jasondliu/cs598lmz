import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

f_c = FUNTYPE(f)

print f_c(2)

def f2(x):
    return x**3

f2_c = FUNTYPE(f2)

print f2_c(2)
</code>
The output is:
<code>4.0
8.0
</code>

