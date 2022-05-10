import ctypes
# Test ctypes.CFUNCTYPE()

# Try calling a function
def func(x, y):
    return y - x

f = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)(func)
assert f(2.0, 3.0) == 1.0
# Try calling a method
class X(object):
    def method(self, x, y):
        return y - x

x = X()
f = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)(x.method)
assert f(2.0, 3.0) == 1.0
# Try calling a function with a custom pointer type
class P(ctypes.Structure):
    _fields_ = [('data', ctypes.c_double)]

def func(p, x, y):
    assert isinstance(p, P)
    return p.data - x + y

f = ctypes.CFUNCTYPE(ctypes.c_double, P, ctypes
