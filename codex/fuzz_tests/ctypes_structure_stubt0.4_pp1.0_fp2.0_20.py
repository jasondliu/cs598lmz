import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

def test_fields():
    s = S()
    s.x = 1
    s.y = 2
    assert s.x == 1
    assert s.y == 2
    assert s.x == s.__dict__["x"]
    assert s.y == s.__dict__["y"]
    assert s.x == getattr(s, "x")
    assert s.y == getattr(s, "y")
    assert s.x == getattr(s, "x")
    assert s.y == getattr(s, "y")
    assert s.x == s._fields_[0][1]._type_._value_
    assert s.y == s._fields_[1][1]._type_._value_
    assert s.x == s._fields_[0][1]._type_._value_
    assert s.y == s._fields_
