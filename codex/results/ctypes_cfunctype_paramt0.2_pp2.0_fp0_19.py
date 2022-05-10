import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(n):
    print "callback called with", n
    return 0

CALLBACK = FUNTYPE(callback)

lib.set_callback(CALLBACK)

lib.call_callback(5)
</code>

