import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint)

def pyfunc(x, y, z):
    print(x, y, z)

f = FUNTYPE(pyfunc)
f(1, 2, 3)
</code>

