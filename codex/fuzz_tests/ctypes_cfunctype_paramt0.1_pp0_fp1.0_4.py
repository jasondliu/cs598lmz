import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("callback called with", x)
    return x + 1

cb = FUNTYPE(my_callback)

lib.call_callback(cb, 1)
</code>

