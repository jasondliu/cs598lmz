import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = C._fields_ + [('y', ctypes.c_int)]

def test_c_field():
    assert type(S.x) is ctypes.CField
    assert isinstance(S.x, ctypes.CField)
    assert isinstance(S.x, ctypes.Field)
    assert S.x.offset == 0
    assert S.x.size == 4
    assert S.x.index == 0
    assert S.x.name == 'x'
    assert S.x.ctype is ctypes.c_int
    assert S.x.type is ctypes.c_int
    assert S.x.__doc__ == 'c_int'
    assert S.x.__name__ == 'x'

    assert D.x.offset == 0
    assert D.x.size == 4
    assert D.x.index == 0
    assert D.x.name == '
