import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(n):
    print("callback called with %d" % n)
    return 0

CALLBACK = FUNTYPE(callback)

lib.call_in_c(CALLBACK)
</code>

