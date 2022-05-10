import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def mycallback(a, b):
    print "mycallback called with", a, b
    return a + b

mycallback_c = FUNTYPE(mycallback)

lib.mycallback = mycallback_c

lib.do_something(1, 2)
</code>

