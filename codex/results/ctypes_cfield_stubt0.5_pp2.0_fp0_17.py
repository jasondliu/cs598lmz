import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_CField():
    assert 'x' in repr(S.x)
    assert 'x' in str(S.x)
    assert 'x' in S.x.__repr__()
    assert 'x' in S.x.__str__()
    assert S.x.__name__ == 'x'
    assert S.x.__qualname__ == 'S.x'
    assert S.x.__module__ == '__main__'
    assert S.x.__objclass__ is S
    assert S.x.__get__(None, S) is S.x
    assert S.x.__get__(S(), S) == 0
    assert S.x.__set__(S(), 3) == None
    assert S.x.__delete__(S()) == None
    assert S.x.__doc__ is None
    assert S.x.offset == 0
    assert S.x.size == 4
    assert S.x.index == 0
    assert S.x.pack == 1
    assert S.x.pack_for
