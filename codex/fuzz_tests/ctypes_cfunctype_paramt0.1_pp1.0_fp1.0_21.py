import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print "callback called with", x
    return x

f = FUNTYPE(callback)

print f(42)
</code>

