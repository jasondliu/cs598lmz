import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def f(x, y):
    return x + y

c_f = FUNTYPE(f)

print(c_f(1, 2))
</code>

