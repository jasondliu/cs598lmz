import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    print "func", a, b
    return a + b

f = FUNTYPE(func)
print f(1, 2)

class X(object):
    def func(self, a, b):
        print "func", a, b
        return a + b

x = X()
f = FUNTYPE(x.func)
print f(1, 2)
</code>

