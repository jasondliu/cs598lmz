import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_get_type():
    assert S.x.get_type() is ctypes.c_int

def test_cfield_get_name():
    assert S.x.get_name() == 'x'

def test_cfield_get_offset():
    assert S.x.get_offset() == 0

def test_cfield_get_size():
    assert S.x.get_size() == 4

def test_cfield_get_bits():
    assert S.x.get_bits() == 32

def test_cfield_get_pack_size():
    assert S.x.get_pack_size() == 4

def test_cfield_get_pack():
    assert S.x.get_pack() == 1

def test_cfield_get_pack_index():
    assert S.x.get_pack_index() == 0

def test_cfield_get_pack_endian():
    assert S.x.get_pack_endian() == '@'

def test_cfield
