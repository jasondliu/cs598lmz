import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.__repr__ = lambda self: 'CField(%r)' % (self.name,)

def test_field_type():
    assert type(S.x) is ctypes.CField

def test_field_name():
    assert S.x.name == 'x'

def test_field_type_name():
    assert S.x.ctype is ctypes.c_int

def test_field_offset():
    assert S.x.offset == ctypes.sizeof(ctypes.c_int)

def test_field_size():
    assert S.x.size == ctypes.sizeof(ctypes.c_int)

def test_field_bits():
    assert S.x.bits == ctypes.sizeof(ctypes.c_int) * 8

def test_field_repr():
    assert repr(S.x) == 'CField(%r)' % (S.x.name,)

def test_field_repr_with_name():
    assert repr(S.x) == '
