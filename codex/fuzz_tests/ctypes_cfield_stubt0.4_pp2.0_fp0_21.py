import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_type():
    assert type(S.x) is ctypes.CField

def test_cfield_name():
    assert S.x.name == 'x'

def test_cfield_type_is_ctype():
    assert isinstance(S.x.ctype, ctypes.CType)

def test_cfield_type_is_ctype_int():
    assert S.x.ctype is ctypes.c_int

def test_cfield_offset():
    assert S.x.offset == ctypes.c_int.size

def test_cfield_index():
    assert S.x.index == 0

def test_cfield_from_address():
    s = S()
    x = ctypes.CField.from_address(ctypes.addressof(s), ctypes.c_int, 'x', 0)
    assert x.name == 'x'
    assert x.ctype is ctypes.c_int
    assert x.offset == ctypes.c_int.size
   
