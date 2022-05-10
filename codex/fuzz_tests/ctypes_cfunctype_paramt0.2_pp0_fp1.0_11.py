import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("callback called with %d" % x)
    return 0

cb = FUNTYPE(my_callback)

lib.register_callback(cb)

print("calling C function")
lib.call_callback()
</code>

