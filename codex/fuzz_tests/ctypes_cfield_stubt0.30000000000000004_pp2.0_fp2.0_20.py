import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert S.x.offset == 0
    assert S.x.size == ctypes.sizeof(ctypes.c_int)
    assert S.x.name == 'x'
    assert S.x.index == 0
    assert S.x.type is ctypes.c_int
    assert S.x.ctype is ctypes.c_int
    assert S.x.pack == 1
    assert S.x.alignment == ctypes.alignment(ctypes.c_int)
    assert S.x.bits == 0
    assert S.x.num == 0
    assert S.x.shape == ()
    assert S.x.strides == ()
    assert S.x.suboffsets == ()
    assert S.x.readonly is False
    assert S.x.raw is False
    assert S.x.pack_for_call is False
    assert S.x.from_address(0) == 0
    assert S.x.from_buffer(b'\x00') == 0
    assert S.x.
