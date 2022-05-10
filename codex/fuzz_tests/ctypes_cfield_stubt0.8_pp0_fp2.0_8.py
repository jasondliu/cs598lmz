import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def make_struct(fields):
    class A(ctypes.Structure):
        _fields_ = fields
    return A

def test_fields():
    for fields in [
        [('a', ctypes.c_int)],
        [('a', ctypes.c_int), ('b', ctypes.c_char)],
        [('a', ctypes.c_int), ('b', ctypes.c_char), ('c', ctypes.c_longlong)],
        [('a', ctypes.c_int), ('b', ctypes.c_char), ('c', ctypes.c_longlong), ('d', ctypes.c_short)],
    ]:
        a = make_struct(fields)
        b = make_struct(list(a._fields_))
        assert isinstance(a, ctypes.Structure)
        assert isinstance(b, ctypes.Structure)
        assert a.__dict__ == b.__dict__

    for fields in [
        [('a', ctypes.c_char, 42)],
