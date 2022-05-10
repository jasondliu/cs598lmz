import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)
def show(x):
    print x

foo=FUNTYPE(show)

foo(5)
</code>

