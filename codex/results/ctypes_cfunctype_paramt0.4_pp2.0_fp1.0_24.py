import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

def callback(a, b):
    print(a, b)

f = FUNTYPE(callback)

lib.register_callback(f)
</code>

