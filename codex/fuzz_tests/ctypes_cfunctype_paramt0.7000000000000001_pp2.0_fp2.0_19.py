import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)

def f(x):
    return x * 2

f_cfunc = FUNTYPE(f)
print(f_cfunc(2))
# 4.0
</code>
The output is <code>4.0</code>.

