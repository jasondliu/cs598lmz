import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_field_type():
    assert S.x.__class__ is ctypes.CField
    assert type(S.x) is ctypes.CField

def test_field_name():
    assert S.x.name == 'x'

def test_field_ctype():
    assert S.x.ctype is ctypes.c_int

def test_field_offset():
    assert S.x.offset == ctypes.sizeof(ctypes.c_int)

def test_field_size():
    assert S.x.size == ctypes.sizeof(ctypes.c_int)

def test_field_index():
    assert S.x.index == 0

def test_field_from_address():
    s = S()
    assert S.x.from_address(ctypes.addressof(s)) == 0

def test_field_from_address_with_offset():
    s = S()
    assert S.x.from_address(ctypes.addressof(s), 1) == 0

def
