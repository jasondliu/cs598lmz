import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(n):
    print 'myfunc(%d)' % n
    return n*n

f = FUNTYPE(myfunc)
print f(10)
</code>
This is a very basic example, but it shows how you can pass the function to some C code.

