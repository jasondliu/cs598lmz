import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_c_field():
    assert isinstance(S.x, ctypes.CField)
    assert S.x.name == 'x'
    assert S.x.type == ctypes.c_int
    assert S.x.offset == 0
    assert S.x.bitsize is None
    assert S.x.bitoffset is None
    assert S.x.in_dll(S, 'x') is S.x
    assert S.x.in_dll(S, 'y') is None
    assert S.x.from_address(id(S.x)) is S.x
    assert S.x.from_address(id(S.x) + 1) is None
    assert S.x.from_address(0) is None
    raises(TypeError, S.x.from_address, 'x')
    raises(TypeError, S.x.in_dll, 'x', 'x')
    raises(TypeError, S.x.in_dll, S, 1)

class S2(ctypes.Structure):
    _fields_
