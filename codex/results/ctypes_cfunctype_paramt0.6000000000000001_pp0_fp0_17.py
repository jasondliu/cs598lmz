import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(i):
    print i
    return 2*i

f = FUNTYPE(callback)
f(2)

</code>

