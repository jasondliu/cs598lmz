import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(a, b):
    print a, b
    return a + b

c_callback = FUNTYPE(callback)

lib.func(c_callback)
</code>

