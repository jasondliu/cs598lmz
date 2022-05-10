import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert isinstance(S.x, ctypes.CField)
    assert S.x.type is ctypes.c_int
    assert S.x.name == 'x'
    assert S.x.offset == 0
    assert S.x.size == ctypes.sizeof(ctypes.c_int)
    assert S.x.index == 0

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

def test_cfield_index():
    assert isinstance(S2.x, ctypes.CField)
    assert S2.x.type is ctypes.c_int
    assert S2.x.name == 'x'
    assert S2.x.offset == 0
    assert S2.x.size == ctypes.sizeof(ctypes.c_int)
    assert S2.x.index == 0

    assert isinstance(S2.y, ctypes.CField)
    assert
