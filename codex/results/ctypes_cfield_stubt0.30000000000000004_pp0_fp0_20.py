import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

def test_field_type():
    assert type(C.x) is ctypes.CField

def test_field_name():
    assert C.x.name == 'x'

def test_field_offset():
    assert C.x.offset == ctypes.sizeof(ctypes.c_int)

def test_field_size():
    assert C.x.size == ctypes.sizeof(ctypes.c_int)

def test_field_ctype():
    assert C.x.ctype is ctypes.c_int

def test_field_from_address():
    c = C()
    assert C.x.from_address(ctypes.addressof(c)) == 0

def test_field_from_address_write():
    c = C()
    C.x.from_address(ctypes.addressof(c)).value = 42
    assert c.x == 42

def test_field
