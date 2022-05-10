import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    # the following should all be true
    assert isinstance(S.x, ctypes.CField)
    assert isinstance(S.x, ctypes.Field)
    assert issubclass(ctypes.CField, ctypes.Field)

def test_cfield_repr():
    assert repr(S.x) == "<CField 'x' of 'S' objects>"

def test_cfield_addressof():
    s = S(42)
    assert ctypes.addressof(s.x) == ctypes.addressof(s) + ctypes.sizeof(ctypes.c_int)

def test_cfield_byref():
    s = S(42)
    assert ctypes.byref(s.x).contents.value == 42

def test_cfield_getattr():
    s = S(42)
    assert s.x == 42

def test_cfield_setattr():
    s = S(42)
    s.x = 24
    assert s.x ==
