import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(i):
    print 'myfunc called with', i
    return i+1

f = FUNTYPE(myfunc)
print f(1)
</code>

