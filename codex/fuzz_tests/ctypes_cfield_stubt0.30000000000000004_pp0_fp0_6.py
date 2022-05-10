import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_c_field():
    assert S.x.__class__ is ctypes.CField
    assert S.x.offset == 0
    assert S.x.size == ctypes.sizeof(ctypes.c_int)
    assert S.x.index == 0
    assert S.x.name == 'x'
    assert S.x.ctype is ctypes.c_int
    assert S.x.type is int
    assert S.x.pack == 1

def test_c_field_repr():
    assert repr(S.x) == '<CField \'x\' of type \'c_int\' at %x>' % (
        id(S.x),)

def test_c_field_get():
    s = S()
    assert s.x == 0
    s.x = 42
    assert s.x == 42

def test_c_field_set():
    s = S()
    s.x = 42
    assert s.x == 42

def test_c_field_set_exception():
   
