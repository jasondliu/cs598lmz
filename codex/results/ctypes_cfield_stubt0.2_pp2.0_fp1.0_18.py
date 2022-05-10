import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert isinstance(S.x, ctypes.CField)
    assert S.x.__name__ == 'x'
    assert S.x.__doc__ == 'c_int'
    assert S.x.__module__ == 'ctypes'
    assert S.x.__objclass__ is S
    assert S.x.__name__ == 'x'
    assert S.x.__repr__() == '<field \'x\' of \'S\' objects>'
    assert S.x.__str__() == 'x'
    assert S.x.__hash__() == hash(S.x.__name__)
    assert S.x.__get__(S()) == 0
    assert S.x.__set__(S(), 1) is None
    assert S.x.__delete__(S()) is None
    assert S.x.offset == 0
    assert S.x.size == 4
    assert S.x.index == 0
    assert S.x.pack == 1
    assert S.x.pack_
