import ctypes

class S(ctypes.Structure):
    x = -42
    def f(self): return self

def test_field_is_callable():
    # access struct attr, check that call returns self
    s = S()
    s.p = S()
    assert S.x.__get__(s) == -42
    assert s.p.f.__call__() is s.p
    assert s.p.f() is s.p

def test_method_is_callable():
    # access struct method, check that call returns self
    s = S()
    assert S().f.__call__() is S()
    assert S().f() is S()
    assert S.f.__get__(s) is s.f
    assert S.f.__get__(s)() is s

class U(object):
    x = 3
    def f(self): return self

def test_method_is_not_callable():
    # regular attr should not be callable
    x = U()
    assert x.x == 3
    raises(TypeError, "x.x.
