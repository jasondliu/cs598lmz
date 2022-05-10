import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(a, b):
    print 'In Python:', a, b
    return a + b

CALLBACK = FUNTYPE(callback)

lib.call_callback(CALLBACK)
</code>

