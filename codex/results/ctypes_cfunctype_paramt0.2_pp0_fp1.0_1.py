import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print(x)
    return x

cb = FUNTYPE(callback)

lib.callback(cb)
</code>

