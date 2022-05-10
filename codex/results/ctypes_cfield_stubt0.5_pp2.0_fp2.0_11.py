import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    field = S.x
    assert field.__name__ == 'x'
    assert field.__class__ is ctypes.CField
    assert field._name == 'x'
    assert field._type_ is ctypes.c_int
    assert field._offset == 0
    assert field._size == ctypes.sizeof(ctypes.c_int)
    assert field._length_ == None
    assert field._index == 0
    assert field._pack_ == 1

    field = S.x
    assert field.__name__ == 'x'
    assert field.__class__ is ctypes.CField
    assert field._name == 'x'
    assert field._type_ is ctypes.c_int
    assert field._offset == 0
    assert field._size == ctypes.sizeof(ctypes.c_int)
    assert field._length_ == None
    assert field._index == 0
    assert field._pack_ == 1

def test_cfield_repr():
    assert repr(S.x) == "<CField '
