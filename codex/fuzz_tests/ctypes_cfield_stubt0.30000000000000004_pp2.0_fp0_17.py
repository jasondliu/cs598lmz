import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_from_address():
    s = S()
    assert S.x.from_address(ctypes.addressof(s)) == s.x

def test_cfield_from_address_offset():
    s = S()
    assert S.x.from_address(ctypes.addressof(s), 1) == (s.x + 1)

def test_cfield_from_address_offset_negative():
    s = S()
    assert S.x.from_address(ctypes.addressof(s), -1) == (s.x - 1)
