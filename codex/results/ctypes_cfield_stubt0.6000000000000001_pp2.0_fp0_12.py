import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_CField():
    assert S.x.__name__ == 'x'
    assert S.x.__doc__ is None
    assert S.x.__module__ == '__main__'
    assert S.x.__objclass__ is S
    assert S.x.__ctype__ is ctypes.c_int
    assert repr(S.x) == "<field 'x' of '__main__.S'>"
    assert isinstance(S.x, ctypes.CField)

def test_CField_set():
    s = S()
    s.x = 42
    assert s.x == 42
    s.x = 'hello'
    assert s.x == ord('h')

def test_CField_get():
    s = S()
    s.x = 42
    assert s.x == 42

def test_CField_by_name():
    assert S.x == S._fields_[0][1]
    assert S.x == S.__dict__['x']
    py.test.raises(
