import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert S.x.__class__ is ctypes.CField

def test_cfield_name():
    assert S.x.name == 'x'

def test_cfield_ctype():
    assert S.x.ctype is ctypes.c_int

def test_cfield_offset():
    assert S.x.offset == 0

def test_cfield_size():
    assert S.x.size == ctypes.sizeof(ctypes.c_int)

def test_cfield_bitsize():
    assert S.x.bitsize == ctypes.sizeof(ctypes.c_int) * 8

def test_cfield_index():
    assert S.x.index == 0

def test_cfield_from_address():
    s = S()
    assert S.x.from_address(ctypes.addressof(s)) == 0

def test_cfield_from_address_write():
    s = S()
    S.x.from_address(ctypes.add
