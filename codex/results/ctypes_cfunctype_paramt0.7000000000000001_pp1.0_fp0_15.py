import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

def cb(i, j):
    print "callback called with ", i, j

cb_func = FUNTYPE(cb)

libc.test(cb_func)
