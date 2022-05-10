import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

def handler(a, b):
    print "handler", a, b

f = FUNTYPE(handler)

lib.test(f)
</code>

