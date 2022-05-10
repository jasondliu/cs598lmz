import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(i):
    print "callback called with", i
    return i + 1

CALLBACK = FUNTYPE(my_callback)

lib.call_in_c(CALLBACK)
</code>

