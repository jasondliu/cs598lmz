import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def cb(n):
    print "cb", n
    return n

cbfun = FUNTYPE(cb)

lib.call_fun(cbfun, 5)
</code>

