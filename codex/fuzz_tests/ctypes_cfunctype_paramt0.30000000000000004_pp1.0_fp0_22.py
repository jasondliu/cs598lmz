import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def foo(x):
    return x + 1

f = FUNTYPE(foo)
print f(42)

# 42
</code>

