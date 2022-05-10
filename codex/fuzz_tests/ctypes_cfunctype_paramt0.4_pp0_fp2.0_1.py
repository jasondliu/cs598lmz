import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(n):
    print "callback called with %d" % n
    return 0

f = FUNTYPE(callback)

lib.set_callback(f)

lib.do_callback(42)
