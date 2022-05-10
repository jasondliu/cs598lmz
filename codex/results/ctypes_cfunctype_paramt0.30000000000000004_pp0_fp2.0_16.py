import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    print "callback called with arg", arg
    return 0

CALLBACK = FUNTYPE(callback)

lib.SetCallback(CALLBACK)

lib.CallCallback(1)
</code>

