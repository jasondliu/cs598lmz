import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert type(S.x) is ctypes.CField

def test_cfield_name():
    assert S.x.name == 'x'

def test_cfield_type():
    assert S.x.type is ctypes.c_int

def test_cfield_offset():
    assert S.x.offset == 0

def test_cfield_from_address():
    s = S()
    x = ctypes.CField.from_address(ctypes.addressof(s), S.x.type)
    assert x.name == 'x'
    assert x.type is ctypes.c_int
    assert x.offset == 0

def test_cfield_from_address_offset():
    s = S()
    x = ctypes.CField.from_address(ctypes.addressof(s), S.x.type, offset=1)
    assert x.name == 'x'
    assert x.type is ctypes.c_int
    assert x.offset == 1

def
