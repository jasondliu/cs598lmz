import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_field_type():
    assert S.x.type is ctypes.c_int

def test_field_name():
    assert S.x.name == 'x'

def test_field_offset():
    assert S.x.offset == ctypes.sizeof(ctypes.c_int)

def test_field_size():
    assert S.x.size == ctypes.sizeof(ctypes.c_int)

def test_field_bitsize():
    assert S.x.bitsize == ctypes.sizeof(ctypes.c_int) * 8

def test_field_pack():
    assert S.x.pack == 1

def test_field_index():
    assert S.x.index == 0

def test_field_flags():
    assert S.x.flags == 0

def test_field_deref():
    assert repr(S.x.dereference()) == '<Field type=int, ofs=0, size=4>'

def test_field_from_address():
    a
