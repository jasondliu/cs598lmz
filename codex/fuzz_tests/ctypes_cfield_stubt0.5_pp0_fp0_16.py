import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    __slots__ = ['x']
    def __init__(self, x):
        self.x = x

class D(object):
    __slots__ = ['x']
    def __init__(self, x):
        self.x = x

def f(x):
    return x

def main():
    x = f(C(1))
    assert type(x) is C
    assert type(x.x) is int
    x = f(D(1))
    assert type(x) is D
    assert type(x.x) is int
    x = f(S(1))
    assert type(x) is S
    assert type(x.x) is ctypes.CField
    x = f(S(1))
    assert type(x) is S
    assert type(x.x) is ctypes.CField

main()
