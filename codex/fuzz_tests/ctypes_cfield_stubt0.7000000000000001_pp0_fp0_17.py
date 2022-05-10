import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

del S, C

def test_basic():
    import _testcapi
    x = _testcapi.new_cfield_int()
    _testcapi.set_cfield_int(x, -3, 42)
    assert x.value == 42
    assert x._objects == {-3: None}
    _testcapi.set_cfield_int(x, -3, -42)
    assert x.value == -42
    assert x._objects == {-3: None}
    y = _testcapi.new_cfield_int()
    _testcapi.set_cfield_int(x, -3, y)
    assert x._objects == {-3: y}
    _testcapi.set_cfield_int(x, -3, None)
    assert x._objects == {}

def test_cfield_from_address():
    import _testcapi
    x = _testcap
