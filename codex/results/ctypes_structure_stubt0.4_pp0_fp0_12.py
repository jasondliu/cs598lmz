import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class C(object):
    _fields_ = [('x', ctypes.c_int)]

def test_struct_type():
    s = S()
    s.x = 42
    assert s.x == 42
    assert s.__dict__ == {}
    py.test.raises(AttributeError, "s.y")
    s.y = 42
    assert s.y == 42
    assert s.__dict__ == {'y': 42}
    s.x = 42
    assert s.x == 42
    assert s.__dict__ == {'y': 42}
    s.y = 43
    assert s.y == 43
    assert s.__dict__ == {'y': 43}
    assert repr(s) == "<test_struct_type.S object at 0x%x>" % (id(s),)

def test_struct_type_with_fields():
    s = S()
    s.x = 42
    assert s.x == 42
    assert s.__dict__ == {}
    py.
