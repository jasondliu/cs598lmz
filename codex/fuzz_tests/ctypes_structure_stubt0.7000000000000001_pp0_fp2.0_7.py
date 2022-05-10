import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    y = ctypes.c_double()

class T(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int)
    ]

class U(ctypes.Union):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int)
    ]

def test_union_base_class():
    class V(U):
        _fields_ = [
            ('foo', ctypes.c_int)
        ]
    assert V.foo.offset == 0

def test_struct():
    s = S()
    assert repr(s) == '<test.test_ctypes_c_struct.S object at %x>' % id(s)
    assert len(s) == ctypes.sizeof(S)
    assert len(s._fields_) == 2
    assert s.x == 0.0
    assert s.y == 0.0
    s.
