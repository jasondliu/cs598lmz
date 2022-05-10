import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def foo(a,b):
    print a,b
    return a+b

foo = FUNTYPE(foo)

foo(1,2)

foo.argtypes = (ctypes.c_int, ctypes.c_int)
foo.restype = ctypes.c_int

print foo(1,2)
</code>

