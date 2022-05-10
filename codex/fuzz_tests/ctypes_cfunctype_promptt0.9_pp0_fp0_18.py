import ctypes
# Test ctypes.CFUNCTYPE(restype, *argtypes)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_double)]

    def __repr__(self):
        return str((self.a, self.b))

class Y(ctypes.Structure):
    _fields_ = [("x", X), ("c", ctypes.c_char)]

    def __repr__(self):
        return str((self.x, self.c))

def f(x):
    x.a = 3
    return x

b = ctypes.CFUNCTYPE(Y, X)(f)

print b.restype
print b.argtypes

y = b(Y(3, 4.0, 'x'))
print y.a, y.b, y.c

try:
    x = (1, 2)
    b = ctypes.CFUNCTYPE(None, X)(x)
except TypeError:
    print "failed"
else:
    assert
