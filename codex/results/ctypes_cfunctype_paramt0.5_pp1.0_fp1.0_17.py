import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)

def c_f(a, b, c, d, e, f):
    return a+b+c+d+e+f

c_func = FUNTYPE(c_f)

def f(a, b, c, d, e, f):
    return a+b+c+d+e+f

py_func = FUNTYPE(f)

@jit(nopython=True)
def jit_f(a, b, c, d, e, f):
    return a+b+c+d+e+f

jit_func = FUNTYPE(jit_f)

x = 1.0
y = 2.0
z = 3.0
w = 4.0
v = 5.0
u = 6.0

print(c_f(x, y, z, w, v, u))
print(f
