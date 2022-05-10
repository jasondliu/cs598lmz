import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print("callback called with", x)
    return x + 1

cb = FUNTYPE(callback)

lib.call_callback(cb, 1)
</code>

