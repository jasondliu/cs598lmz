import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_CField_get():
    assert S.x.get(S(42)) == 42

def test_CField_set():
    s = S()
    S.x.set(s, 42)
    assert s.x == 42

def test_CField_get_address():
    s = S(42)
    assert S.x.get_address(s) == ctypes.addressof(s.x)

def test_CField_get_address_simple():
    s = S(42)
    assert S.x.get_address_simple(s) == ctypes.addressof(s.x)

def test_CField_get_address_simple_offset():
    s = S(42)
    assert S.x.get_address_simple_offset(s) in [
        ctypes.addressof(s.x) - 1,
        ctypes.addressof(s.x),
        ctypes.addressof(s.x) + 1]

def test_CField_get_address_
