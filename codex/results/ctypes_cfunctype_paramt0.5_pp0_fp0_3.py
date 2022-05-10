import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_float)

def callme(x, y, z):
    print x, y, z

f = FUNTYPE(callme)
f(1, 2, 3.0)
</code>

