import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert type(S.x) is ctypes.CField
    assert S.x.offset == 0
    assert S.x.size == ctypes.sizeof(ctypes.c_int)
    assert S.x.index == 0
    assert S.x.bitshift == 0
    assert S.x.bitsize == ctypes.sizeof(ctypes.c_int) * 8
    assert S.x.type is ctypes.c_int
    assert S.x.name == 'x'
    assert S.x.pack == 1
    assert S.x.pack_bigendian == False
    assert S.x.pack_littleendian == False
    assert S.x.pack_msb == False
    assert S.x.pack_lsb == False
    assert S.x.pack_signed == False
    assert S.x.pack_unsigned == False
    assert S.x.pack_float == False
    assert S.x.pack_char == False
    assert S.x.pack_bool == False
    assert
