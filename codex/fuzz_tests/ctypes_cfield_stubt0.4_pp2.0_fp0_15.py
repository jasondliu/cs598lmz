import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_field_type():
    assert type(S.x) is ctypes.CField

def test_field_name():
    assert S.x.name == 'x'

def test_field_type_name():
    assert S.x.type_name == 'c_int'

def test_field_type_is_c_int():
    assert S.x.type is ctypes.c_int

def test_field_offset():
    assert S.x.offset == ctypes.sizeof(ctypes.c_int)

def test_field_size():
    assert S.x.size == ctypes.sizeof(ctypes.c_int)

def test_field_bitsize():
    assert S.x.bitsize == 8 * ctypes.sizeof(ctypes.c_int)

def test_field_from_address():
    s = S()
    s.x = 42
    assert S.x.from_address(ctypes.addressof(s)).value == 42
