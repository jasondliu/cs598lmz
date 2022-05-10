import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_c_field():
    s = S()
    s.x = 42
    assert s.x == 42
    assert type(s.x) is ctypes.CField
    assert ctypes.CField(s, 'x') == 42

def test_c_field_set():
    s = S()
    s.x = 42
    assert s.x == 42
    s.x = 24
    assert s.x == 24

def test_c_field_from_param():
    s = S()
    s.x = 42
    assert ctypes.CField.from_param(s.x) == 42
    assert ctypes.CField.from_param(s.x) == 42

def test_c_field_get_set():
    s = S()
    s.x = 42
    assert s.x == 42
    assert ctypes.CField.get(s, 'x') == 42
    ctypes.CField.set(s, 'x', 24)
    assert ctypes.CField.get(s, '
