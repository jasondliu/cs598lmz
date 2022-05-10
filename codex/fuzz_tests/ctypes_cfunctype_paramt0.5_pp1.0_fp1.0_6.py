import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    print 'myfunc called with', x
    return x + 1

f = FUNTYPE(myfunc)

print f(5)

print 'done'
