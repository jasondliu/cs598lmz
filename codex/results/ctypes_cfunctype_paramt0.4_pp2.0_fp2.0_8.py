import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def foo(x):
    print 'foo called with', x
    return x

fptr = FUNTYPE(foo)
fptr(42)
</code>

