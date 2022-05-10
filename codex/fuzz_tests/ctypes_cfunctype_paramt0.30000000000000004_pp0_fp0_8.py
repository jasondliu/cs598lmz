import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(a, b):
    print 'in python callback', a, b
    return a + b

cb = FUNTYPE(callback)

lib.call_back(cb)
</code>

