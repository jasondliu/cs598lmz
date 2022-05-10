import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert isinstance(S.x, ctypes.CField)
    assert S.x.type is ctypes.c_int
    assert S.x.offset == 0
    assert S.x.size == ctypes.sizeof(ctypes.c_int)
    assert S.x.name == 'x'
    assert S.x.pack == 1
    assert S.x.bitsize == 0
    assert S.x.bitoffset == 0
    assert S.x.is_bitfield == False
    assert S.x.is_static == False
    assert S.x.is_volatile == False
    assert S.x.is_const == False
    assert S.x.is_restrict == False
    assert S.x.has_index == False
    assert S.x.index == 0
    assert S.x.has_length == False
    assert S.x.length == 0
    assert S.x.has_alignment == False
    assert S.x.alignment == 0
    assert S.x.has_
