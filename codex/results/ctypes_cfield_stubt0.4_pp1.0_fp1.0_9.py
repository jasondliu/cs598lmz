import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    # ctypes.CField is a subclass of ctypes.Field,
    # and therefore has a _type_ attribute.
    assert type(S.x) is ctypes.CField
    assert S.x._type_ is ctypes.c_int
    assert type(S.x._type_) is type(ctypes.c_int)
    assert S.x._type_ is int

def test_cfield_repr():
    # ctypes.CField.__repr__() should not raise an exception
    repr(S.x)

def test_cfield_set():
    # ctypes.CField.__set__() should not raise an exception
    S.x.__set__(S(), 1)

def test_cfield_get():
    # ctypes.CField.__get__() should not raise an exception
    S.x.__get__(S(), S)

def test_cfield_delete():
    # ctypes.CField.__delete__() should not raise an exception
    S.
