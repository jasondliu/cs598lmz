import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print "callback called with", x
    return x

CALLBACK = FUNTYPE(callback)

lib = ctypes.CDLL("./libtest.so")
lib.test(CALLBACK)
</code>

