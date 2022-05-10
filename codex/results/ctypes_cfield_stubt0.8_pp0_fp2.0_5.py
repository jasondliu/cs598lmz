import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(object):
    def __init__(self, val):
        self.field = val

class Y(object):
    def __init__(self, val):
        self.field = ctypes.c_int(val)

class Z(object):
    def __init__(self, val):
        self.field = ctypes.CField(val)


def test_ctypes_field(benchmark):
    def f():
        x = X(3)
        return x.field
    benchmark(f)

def test_int(benc
