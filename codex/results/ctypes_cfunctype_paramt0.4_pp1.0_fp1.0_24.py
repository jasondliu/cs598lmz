import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(a, b):
    print "callback:", a, b
    return a + b

cb = FUNTYPE(callback)

lib.call_me(cb)
</code>

