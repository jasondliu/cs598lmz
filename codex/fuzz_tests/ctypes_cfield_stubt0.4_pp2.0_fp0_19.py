import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    s = S()
    s.x = 42
    assert s.x == 42
    assert type(s.x) is ctypes.c_int
    assert type(S.x) is ctypes.CField
    assert S.x.__name__ == 'x'
    assert S.x.__dict__ == {}
    assert S.x.__doc__ is None
    assert S.x.__module__ == '__main__'
    assert S.x.offset == ctypes.sizeof(ctypes.c_int)
    assert S.x.size == ctypes.sizeof(ctypes.c_int)
    assert repr(S.x) == "<Field type=c_int, ofs=0, size=4>"
    raises(AttributeError, "S.x.value")
    raises(AttributeError, "S.x.index")
    raises(AttributeError, "S.x.pack")
    raises(AttributeError, "S.x.unpack")
    raises(AttributeError, "S.x.get
