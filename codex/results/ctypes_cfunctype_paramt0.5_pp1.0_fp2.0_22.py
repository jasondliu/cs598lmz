import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)
def cb_func(a,b):
    print(a,b)
    return 0

cb = FUNTYPE(cb_func)

lib.set_callback(cb)
lib.call_callback()
</code>

