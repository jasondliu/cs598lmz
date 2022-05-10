import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print("callback", x)
    return x

cb = FUNTYPE(callback)

lib.call_callback(cb, 10)
</code>

