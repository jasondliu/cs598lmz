import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

class Function(object):
    def __init__(self, f, argtypes, restype):
        self.f = FUNTYPE(restype, *argtypes)(f)
    def __call__(self, *args):
        return self.f(*args)

def f(x, y):
    return x+y

g = Function(f, [ctypes.c_double, ctypes.c_double], ctypes.c_double)

print g(1,2)
</code>

