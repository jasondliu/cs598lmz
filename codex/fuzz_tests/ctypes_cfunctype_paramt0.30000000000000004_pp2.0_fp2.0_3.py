import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def foo(x, y):
    return x + y

foo_c = FUNTYPE(foo)
print foo_c(1, 2)
</code>

