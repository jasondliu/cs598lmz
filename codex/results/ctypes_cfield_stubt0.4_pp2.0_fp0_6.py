import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

class D(C):
    def __init__(self, x):
        C.__init__(self, x)

def f(x):
    return x

def g(x):
    return x

def h(x):
    return x

def test_field():
    assert f(S.x) is S.x
    assert g(S.x) is S.x
    assert h(S.x) is S.x

def test_instance_attr():
    s = S()
    assert f(s.x) is s.x
    assert g(s.x) is s.x
    assert h(s.x) is s.x

def test_class_attr():
    assert f(C.x) is C.x
    assert g(C.x) is C.x
    assert h(C.x) is C.x

def test_instance_attr_subclass():
    c = C(42
