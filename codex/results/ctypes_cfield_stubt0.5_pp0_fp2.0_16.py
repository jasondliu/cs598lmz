import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_CField():
    class S(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int)]

    ctypes.CField = type(S.x)

    # test 'value'
    s = S()
    s.x = 42
    assert s.x == 42
    assert s.x.value == 42
    s.x.value = 42
    assert s.x == 42

    # test '_type_'
    assert s.x._type_ == ctypes.c_int
    assert s.x._type_ is ctypes.c_int

    # test '_name_'
    assert s.x._name_ == 'x'
    assert s.x._name_ is 'x'

def test_CField_repack():
    class S(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int)]

    ctypes.CField = type(S.x)

    # test 'value'
    s = S()
    s.x = 42

