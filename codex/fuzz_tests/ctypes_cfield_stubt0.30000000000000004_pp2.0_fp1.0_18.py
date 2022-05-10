import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

def test_cfield_from_param():
    assert ctypes.CField.from_param(S.x) is S.x
    assert ctypes.CField.from_param(S.x) is not C.x
    assert ctypes.CField.from_param(S.x) == S.x
    assert ctypes.CField.from_param(S.x) != C.x
    assert ctypes.CField.from_param(S.x).__class__ is ctypes.CField

def test_cfield_get_field_name():
    assert S.x.get_field_name() == 'x'

def test_cfield_get_field_type():
    assert S.x.get_field_type() is ctypes.c_int

def test_cfield_get_size():
    assert S.x.get_size() == ctypes.sizeof(ctypes.c_int)


