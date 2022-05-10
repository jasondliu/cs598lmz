import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_type():
    assert type(S.x) is ctypes.CField

def test_cfield_get_type():
    assert S.x._type_ is ctypes.c_int

def test_cfield_get_name():
    assert S.x.name == 'x'

def test_cfield_get_offset():
    assert S.x.offset == ctypes.sizeof(ctypes.c_int)

def test_cfield_get_size():
    assert S.x.size == ctypes.sizeof(ctypes.c_int)

def test_cfield_get_index():
    assert S.x.index == 0

def test_cfield_get_pack():
    assert S.x.pack == 1

def test_cfield_set_type():
    S.x._type_ = ctypes.c_long
    assert S.x._type_ is ctypes.c_long
    assert S.x.size == ctypes.sizeof(ctypes.c_long)

