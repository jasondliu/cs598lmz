import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)
def f(i):
    print i

fptr = FUNTYPE(f)
fptr(42)
</code>

