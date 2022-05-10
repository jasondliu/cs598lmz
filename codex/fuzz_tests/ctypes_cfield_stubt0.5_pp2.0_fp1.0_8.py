import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class T(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

def test_c_field():
    assert type(T.x) is ctypes.CField

class U(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

def test_c_union_field():
    assert type(U.x) is ctypes.CField

def test_c_field_repr():
    assert repr(S.x) == "<Field type=c_int, ofs=0, size=4>"

def test_c_field_name():
    assert S.x.name == 'x'

def test_c_field_ctype():
    assert S.x.ctype is ctypes.c_int

def test_c_field_offset():
    assert S.x.offset == 0

def test_c_field_size():
    assert S.x.size == 4

def test_c_field_from_address():
    s = S
