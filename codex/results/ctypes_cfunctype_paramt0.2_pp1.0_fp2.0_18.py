import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    print(a, b)
    return a + b

f = FUNTYPE(func)
print(f(1, 2))
</code>

