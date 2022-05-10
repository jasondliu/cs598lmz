import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(i):
    print "callback", i
    return 0

cb = FUNTYPE(my_callback)

c_lib.call_func(cb)
</code>

