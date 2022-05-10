import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    # Test ctypes.CField

    assert isinstance(S.x, ctypes.CField)
    assert S.x.offset == 0
    assert S.x.size == ctypes.sizeof(ctypes.c_int)
    assert S.x.name == 'x'
    assert S.x.ctype is ctypes.c_int
    assert S.x.type == ctypes.c_int
    assert S.x.index == 0
    assert S.x.pack == 1
    assert S.x.bitsize == None
    assert S.x.bitoffset == None
    assert S.x.is_bitfield == False

    # test a bitfield
    class S(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int, 1)]

    assert isinstance(S.x, ctypes.CField)
    assert S.x.offset == 0
    assert S.x.size == ctypes.sizeof(ctypes.c_int)
    assert S.x.
