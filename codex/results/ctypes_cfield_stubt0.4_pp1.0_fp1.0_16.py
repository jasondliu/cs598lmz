import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_instance():
    assert isinstance(S.x, ctypes.CField)

def test_cfield_type():
    assert type(S.x) is ctypes.CField

def test_cfield_repr():
    assert repr(S.x) == "<CField 'x' of type 'c_int'>"

def test_cfield_name():
    assert S.x.name == 'x'

def test_cfield_ctype():
    assert S.x.ctype is ctypes.c_int

def test_cfield_offset():
    assert S.x.offset == ctypes.sizeof(ctypes.c_int)

def test_cfield_bitsize():
    assert S.x.bitsize == ctypes.sizeof(ctypes.c_int) * 8

def test_cfield_from_address():
    s = S()
    assert ctypes.CField.from_address(id(s)).name == 'x'

def test_cfield_from_address_
