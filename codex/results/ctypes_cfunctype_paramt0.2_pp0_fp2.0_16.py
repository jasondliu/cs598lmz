import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print "callback called with arg", arg
    return 0

CALLBACK = FUNTYPE(callback)

lib.set_callback(CALLBACK)

lib.call_callback(5)
</code>

