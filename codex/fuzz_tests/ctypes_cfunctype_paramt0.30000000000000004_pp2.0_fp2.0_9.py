import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def make_callback(f):
    return FUNTYPE(f)

def callback(n):
    print 'callback called with', n
    return n * 2

cb = make_callback(callback)
print cb(2)
</code>

