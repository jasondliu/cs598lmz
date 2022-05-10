import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert S.x.__doc__ == 'C integer'
    assert S.x.__name__ == 'x'
    assert S.x.__repr__() == '<Field type=c_int, ofs=0, size=4>'
    assert S.x.__hash__() == hash(S.x.__repr__())
    assert S.x.__get__(S(1)) == 1
    assert S.x.__set__(S(1), 2) == None
    assert S(2).x == 2
    raises(AttributeError, "S.x.__delete__(S(1))")
    raises(AttributeError, "S.x.__set__(S(1), 'x')")
    raises(AttributeError, "S.x.__set__(S(1), 1.5)")
    raises(AttributeError, "S.x.__set__(S(1), 2**100)")
    raises(AttributeError, "S.x.__set__(S(1), -(
