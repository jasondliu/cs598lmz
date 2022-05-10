import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert type(S.x) is ctypes.CField
    assert S.x.__name__ == 'x'
    assert S.x.__doc__ == 'c_int'
    assert S.x.__module__ == 'ctypes'
    assert S.x.__get__(S(42)) == 42
    assert S.x.__set__(S(42), 43) == None
    assert S.x.__delete__(S(42)) == None
    assert S.x.offset == ctypes.c_int.offset
    assert S.x.size == ctypes.c_int.size

def test_cfield_attributes():
    assert S.x.offset == ctypes.c_int.offset
    assert S.x.size == ctypes.c_int.size
    assert S.x.index == 0
    assert S.x.pack == 1
    assert S.x.type == ctypes.c_int

def test_cfield_setattr():
    raises(AttributeError, "S
