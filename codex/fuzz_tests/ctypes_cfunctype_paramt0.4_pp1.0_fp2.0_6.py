import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print 'in callback:', x
    return x

cb = FUNTYPE(callback)

print 'in main:', cb(42)
</code>

