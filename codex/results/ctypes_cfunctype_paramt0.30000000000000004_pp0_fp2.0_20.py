import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def make_callback(f):
    return FUNTYPE(f)

def callback(x):
    print 'callback called with', x
    return x + 1

cb = make_callback(callback)
print cb(1)
</code>

