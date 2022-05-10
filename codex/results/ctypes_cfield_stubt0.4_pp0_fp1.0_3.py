import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert isinstance(S.x, ctypes.CField)
    assert S.x.__name__ == 'x'
    assert S.x.offset == 0
    assert S.x.size == ctypes.sizeof(ctypes.c_int)
    assert S.x.ctype is ctypes.c_int
    assert S.x.type is int
    assert S.x.index == 0
    assert S.x.pack == 1
    assert S.x.bitsize == 0
    assert S.x.bitoffset == 0
    assert S.x.shape == None
    assert S.x.in_dll(S, 'x') is S.x

def test_cfield_get_set():
    s = S(42)
    assert s.x == 42
    s.x = 0
    assert s.x == 0

def test_cfield_get_set_array():
    class S(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int * 4)]
