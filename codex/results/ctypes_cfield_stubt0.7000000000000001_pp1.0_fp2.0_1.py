import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_c_int():
    v = ctypes.c_int(42)
    assert type(v) is ctypes.c_int
    assert v.value == 42
    assert v.__doc__ == "c_int(42)"
    assert repr(v) == "c_int(42)"
    v.value = -42
    assert v.value == -42
    raises(TypeError, setattr, v, 'value', 'hello')
    raises(TypeError, setattr, v, 'value', 2**100)

def test_c_void_p():
    v = ctypes.c_void_p(42)
    assert type(v) is ctypes.c_void_p
    assert v.value == 42
    v.value = -42
    assert v.value == -42
    raises(TypeError, setattr, v, 'value', 'hello')

def test_value():
    import sys
    v = ctypes.c_int()
    assert v.value == 0
    v = ctypes.c_int(
