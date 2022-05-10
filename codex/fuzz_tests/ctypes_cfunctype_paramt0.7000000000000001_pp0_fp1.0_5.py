import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def g(x):
    return x*x

f = FUNTYPE(g)
print f(2.0)

class MyClass(object):
    def __init__(self):
        self._f = FUNTYPE(self._g)

    def _g(self, x):
        return x*x

    def f(self, x):
        return self._f(x)

m = MyClass()
print m.f(2.0)
</code>

