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
    assert S.x.offset == ctypes.sizeof(ctypes.c_int)
    assert S.x.size == ctypes.sizeof(ctypes.c_int)
    assert S.x.index == 0
    assert S.x.name == 'x'
    assert S.x.ctype is ctypes.c_int

if __name__ == "__main__":
    test_cfield()
