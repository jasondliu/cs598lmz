import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_long)

def foo():
    return 1

f = FUNTYPE(foo)

print f() # prints 1

def bar():
    return 2

f.restype = ctypes.c_int
f.argtypes = []
f.__name__ = "bar"

print f() # prints 2
</code>

