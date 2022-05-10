import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_field(x):
    assert type(x) is ctypes.CField
    assert repr(x) == "<Field x of type <class 'ctypes.c_int'>"
    assert str(x) == "x"
    assert x.name == "x"
    assert x.ctype is ctypes.c_int
    assert x.offset == 0
    assert x.size == 4

def test_cfield():
    f = S.x
    test_field(f)

    assert S._fields_[0] is f
    assert S._fields_[0].offset == 0
    assert S._fields_[0].size == 4

def test_array():
    at = ctypes.c_int * 17
    assert at._length_ == 17
    assert repr(at) == "<class 'ctypes.c_int[17]'>"
    assert str(at) == "c_int_Array_17"
    assert type(at._type_) is ctypes.CField
    assert type(at._type_) is ctypes.C
