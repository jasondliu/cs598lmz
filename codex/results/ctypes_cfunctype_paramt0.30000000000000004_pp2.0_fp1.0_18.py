import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def cb(a, b):
    print "callback called with", a, b
    return a + b

cb_func = FUNTYPE(cb)

lib.call_func(cb_func)
</code>

