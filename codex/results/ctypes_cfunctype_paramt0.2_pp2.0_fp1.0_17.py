import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print "callback called with", x
    return x

cb = FUNTYPE(callback)

lib.call_back(cb)
</code>

