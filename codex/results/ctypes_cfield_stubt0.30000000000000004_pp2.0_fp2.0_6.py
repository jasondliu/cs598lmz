import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert isinstance(S.x, ctypes.CField)
    assert S.x.__name__ == 'x'
    assert S.x.__module__ == '__main__'
    assert S.x.__objclass__ is S
    assert S.x.__repr__() == '<field x of type c_int>'
    assert S.x.__str__() == '<field x of type c_int>'
    assert S.x.__hash__() == hash(S.x.__name__)
    assert S.x.__get__(S()) == 0
    assert S.x.__get__(S(1)) == 1
    assert S.x.__get__(None, S) is S.x
    assert S.x.__set__(S(), 1) is None
    assert S().x == 1
    raises(AttributeError, "S.x.__set__(None, 1)")
    raises(AttributeError, "S.x.__set__(S(), 'abc')")
