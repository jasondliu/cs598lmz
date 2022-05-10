import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def get_c_function(fun):
    return FUNTYPE(fun)

def f(x):
    return x*x

f_c = get_c_function(f)

print f_c(3)

def g(x):
    return x*x*x

g_c = get_c_function(g)

print g_c(3)
</code>
This will print:
<code>9.0
27.0
</code>

