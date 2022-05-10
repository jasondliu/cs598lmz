import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert type(S.x) is ctypes.CField
    assert S.x.offset == 0
    assert S.x.size == ctypes.sizeof(ctypes.c_int)
    assert S.x.index == 0
    assert S.x.bitsize is None
    assert S.x.bitoffset is None
    assert S.x.type is ctypes.c_int
    assert S.x.name == 'x'
    assert S.x.pack == 1
    assert S.x.ctype is ctypes.c_int
    assert S.x.is_array == False
    assert S.x.is_pointer == False
    assert S.x.is_volatile == False
    assert S.x.is_restrict == False
    assert S.x.is_static == False
    assert S.x.is_const == False
    assert S.x.is_atomic == False
    assert S.x.is_bitfield == False
    assert S.x.is_flexible_array == False

