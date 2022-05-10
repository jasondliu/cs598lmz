import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def my_callback(x):
    print("callback called with %d" % x)
    return x**2
cb = FUNTYPE(my_callback)

lib.set_callback(cb)

lib.call_callback(1)
</code>

