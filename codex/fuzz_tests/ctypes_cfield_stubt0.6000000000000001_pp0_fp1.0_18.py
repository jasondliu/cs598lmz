import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def get_field_type(obj, name):
    field = getattr(obj, name)
    assert isinstance(field, ctypes.CField)
    return field.__class__

def test():
    s = S()
    s.x = 42
    assert s.x == 42
    assert get_field_type(s, 'x') is ctypes.c_int
    s.x = "hello"
    assert s.x == 0
    assert get_field_type(s, 'x') is ctypes.c_int

test()
