import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

def test_cfield():
    x = S.x
    assert x._name == 'x'
    assert x._type_ == ctypes.c_int
    assert x._offset == 0
    assert x._length == 4
    assert x._sizeofinstanc
