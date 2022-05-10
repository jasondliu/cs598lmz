import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(i):
    print "callback", i
    return i

f = FUNTYPE(callback)

print f(1)
</code>

