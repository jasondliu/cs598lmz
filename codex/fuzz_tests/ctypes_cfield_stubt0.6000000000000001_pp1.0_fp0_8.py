import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_field_type():
    assert isinstance(S.x, ctypes.CField)

def test_field_name():
    assert S.x.name == 'x'

def test_field_type_name():
    assert S.x.ctype.__name__ == 'c_int'

def test_field_offset():
    assert S.x.offset == ctypes.sizeof(ctypes.c_int)

def test_field_size():
    assert S.x.size == ctypes.sizeof(ctypes.c_int)

def test_field_index():
    assert S.x.index == 0

def test_field_bits():
    assert S.x.bits == 32

def test_contains():
    assert 'x' in S._fields_

def test_get_item():
    assert S._fields_['x'] is S.x
