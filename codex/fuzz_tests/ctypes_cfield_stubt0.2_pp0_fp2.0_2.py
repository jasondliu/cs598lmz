import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert isinstance(S.x, ctypes.CField)
    assert S.x.__name__ == 'x'
    assert S.x.__module__ == '__main__'
    assert S.x.__qualname__ == 'S.x'
    assert S.x.__objclass__ is S
    assert S.x.__ctype__ is ctypes.c_int
    assert S.x.__offset__ == 0
    assert S.x.__index__ == 0
    assert S.x.__doc__ == 'x'
    assert S.x.__hash__() == hash(S.x)
    assert S.x.__repr__() == '<Field type=c_int, ofs=0: x>'
    assert S.x.__str__() == 'x'
    assert S.x.__eq__(S.x)
    assert not S.x.__eq__(S.x.__class__)
    assert not S.x.__eq__(None)
    assert
