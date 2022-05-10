import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
assert isinstance(S.x, ctypes.CField)

f = S.x
assert f.offset == 0
assert f.size == 4
assert f.name == 'x'
assert f.ctype is ctypes.c_int
assert f.type is int

py.test.raises(AttributeError, 'f.bits')
py.test.raises(AttributeError, 'f.index')

def test_fields_list(size=sizeof(ctypes.c_int)):
    f = (ctypes.c_byte * size)(1, 2, 3, 4, 5)
    assert list(f) == [1, 2, 3, 4, 5]
    f = (ctypes.c_short * (size/2))(1, 2, 3, 4, 5)
    assert list(f) == [1, 2, 3, 4, 5]
    if size == 8:
        f = (ctypes.c_long * (size/4))(1, 2, 3, 4, 5)
        assert list(f) == [1
