import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_c_field():
    assert isinstance(S.x, ctypes.CField)
    assert S.x.__name__ == 'x'
    assert S.x.__doc__ == None
    assert S.x.__module__ == '__main__'
    assert S.x.__objclass__ is S
    assert S.x.__qualname__ == 'S.x'
    assert S.x.type is ctypes.c_int
    assert S.x.offset == 0
    assert S.x.size == 4
    assert S.x.index == 0
    assert repr(S.x) == '<CField type=c_int, ofs=0:0, size=4>'

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

def test_c_field_2():
    assert isinstance(S2.x, ctypes.CField)
    assert S2.x.__name__ ==
