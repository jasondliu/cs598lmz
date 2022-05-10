import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
def test_cfield_set_computed_size():
    with raises(TypeError):
        S.x.size = 4

class S(ctypes.Structure):
    pass

S._fields_ = [('x', ctypes.c_int)]
S.x.size = 4
assert S.x.size == ctypes.sizeof(ctypes.c_int)
