import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(a):
    print "Callback called with", a
    return 0

CALLBACK = FUNTYPE(my_callback)

lib.set_callback(CALLBACK)
</code>

