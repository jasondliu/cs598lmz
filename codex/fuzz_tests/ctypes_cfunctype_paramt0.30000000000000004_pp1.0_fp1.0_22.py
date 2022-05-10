import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print 'Python callback:', x
    return x*x

cb = FUNTYPE(callback)

lib = ctypes.CDLL('./libfoo.so')
lib.foo(cb)
</code>

