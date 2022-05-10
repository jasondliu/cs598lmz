import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert isinstance(S.x, ctypes.CField)
    assert S.x.__name__ == 'x'
    assert S.x.__qualname__ == 'S.x'
    assert S.x.__module__ == '__main__'
    assert S.x.__doc__ == None
    assert S.x.__dict__ == {}
    assert S.x.__class__ == ctypes.CField
    assert S.x.__get__(S(42)) == 42
    assert S.x.__set__(S(42), 43) == None
    assert S(42).x == 43
    assert S.x.__delete__(S(42)) == None
    assert S(42).x == 0

def test_cfield_descriptor():
    class C(type):
        def __getattr__(cls, name):
            return 42
    class D(metaclass=C):
        x = S.x
    assert D.x == 42

def test_cfield_met
