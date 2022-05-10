import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(val):
    print "callback called with %d" % val
    return val

cfunc = FUNTYPE(callback)

lib.run_callback(cfunc)
</code>

