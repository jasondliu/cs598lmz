import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    s = S()
    s.x = 3
    assert s.x == 3
    assert type(s.x) is ctypes.c_int
    assert type(s.x) is ctypes.CField
    assert type(s.x) is not ctypes.c_int32

def test_cfield_subclass():
    class S2(S):
        pass
    s = S2()
    s.x = 3
    assert s.x == 3
    assert type(s.x) is ctypes.c_int
    assert type(s.x) is ctypes.CField
    assert type(s.x) is not ctypes.c_int32

def test_cfield_subclass_with_new_fields():
    class S2(S):
        _fields_ = [('y', ctypes.c_int)]
    s = S2()
    s.x = 3
    assert s.x == 3
    assert type(s.x) is ctypes.c_int
    assert type
