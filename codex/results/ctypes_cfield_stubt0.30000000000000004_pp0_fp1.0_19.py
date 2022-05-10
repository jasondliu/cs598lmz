import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert S.x.__doc__ == 'C integer'
    assert S.x.__name__ == 'x'
    assert S.x.__module__ == 'ctypes'
    assert S.x.__class__ is ctypes.CField
    assert S.x.__dict__ is S.x._field_
    assert S.x._type_ is ctypes.c_int
    assert S.x._name is S.x.__name__
    assert S.x._offset == 0
    assert S.x._size == 4
    assert S.x._index == 0
    assert S.x._pack_ == 1
    assert S.x._alignment == 1
    assert S.x._length_ == 1
    assert S.x._length_ == 1
    assert S.x._length_ == 1
    assert S.x._length_ == 1
    assert S.x._length_ == 1
    assert S.x._length_ == 1
    assert S.x._length_ == 1
    assert S.x._length_
