import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

def test_field_by_name():
    o = S()
    o.x = 42
    o.y = -42
    assert o.x == 42
    assert o.y == -42
    assert o['x'] == 42
    assert o['y'] == -42
    assert o[0] == 42
    assert o[1] == -42
    assert o[-2] == 42
    assert o[-1] == -42
    raises(IndexError, o.__getitem__, 2)
    raises(IndexError, o.__getitem__, -3)
    raises(TypeError, o.__getitem__, 'x')
    raises(TypeError, o.__getitem__, 42)

def test_field_by_index():
    o = S()
    o[0] = 42
    o[1] = -42
    assert o.x == 42

