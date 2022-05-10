import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_type_equality():
    ctypes.c_int(3) == 3

def test_invalid_type():
    raises(TypeError, ctypes.c_int, "hello")

def test_set_invalid_value():
    s = S()
    raises(TypeError, 's.x = "hello"')

def test_instance():
    ctypes.c_int(3)

def test_getattr():
    ctypes.c_int.__ctype_be__

def test_setattr():
    raises(AttributeError, 'ctypes.c_int.__ctype_be__ = 3')

def test_get_field():
    S._fields_[0] == ("x", ctypes.c_int)

def test_set_field():
    raises(AttributeError, 'S._fields_[0] = 3')

def test_get_fields():
    S._fields_ == [("x", ctypes.c_int)]

def test_set_fields():
    raises(AttributeError,
