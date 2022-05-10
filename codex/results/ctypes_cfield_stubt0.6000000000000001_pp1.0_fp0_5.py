import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_field_type():
    assert S.x.__class__ == ctypes.CField

def test_field_name():
    assert S.x.name == 'x'

def test_field_type_name():
    assert S.x.type_name == 'c_int'

def test_field_type_is_ctype():
    assert isinstance(S.x.ctype, ctypes.CType)

def test_field_type_is_int():
    assert S.x.ctype == ctypes.c_int

def test_field_offset():
    assert S.x.offset == ctypes.sizeof(ctypes.c_long)

def test_field_size():
    assert S.x.size == ctypes.sizeof(ctypes.c_int)

def test_field_index():
    assert S.x.index == 0

def test_field_bits():
    assert S.x.bits == 0

def test_field_from_address():
    s = S.from_address
