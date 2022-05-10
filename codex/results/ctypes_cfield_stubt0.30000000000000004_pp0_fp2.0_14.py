import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_CField():
    assert isinstance(S.x, ctypes.CField)
    assert S.x.__name__ == 'x'
    assert S.x.__qualname__ == 'S.x'
    assert S.x.__objclass__ is S
    assert S.x.__ctype__ is ctypes.c_int
    assert S.x.__offset__ == 0
    assert S.x.__index__ == 0
    assert S.x.__doc__ == 'x'

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

def test_CField_index():
    assert S2.x.__index__ == 0
    assert S2.y.__index__ == 1

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int)]

