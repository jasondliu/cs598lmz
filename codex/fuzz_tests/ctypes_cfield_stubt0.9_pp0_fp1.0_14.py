import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_c_field():
    assert ctypes.CField.__module__ == "ctypes"
    assert isinstance(ctypes.CField, type)
    assert issubclass(ctypes.CField, object)
    assert not hasattr(ctypes.CField, '__new__')

def test_c_field_attributes():
    f = S.x
    assert f.__class__ == ctypes.CField
    assert f.name == 'x'
    assert f.ctype == ctypes.c_int

# a c_int is a subclass of ctypes.CFunctype
class C(ctypes.c_int):
    pass

def test_c_field_base_type():
    f = S.x
    assert f.__base__ == ctypes.c_int
    assert type(f) == ctypes.CField
    assert issubclass(C, ctypes.c_int)
    assert issubclass(C, ctypes.CFuncPtr)

def test_c_field_is_type():

