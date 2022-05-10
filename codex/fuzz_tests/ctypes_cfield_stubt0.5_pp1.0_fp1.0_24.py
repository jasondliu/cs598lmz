import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    with pytest.raises(TypeError):
        type(S.x)()
    with pytest.raises(TypeError):
        type(S.x)(1)
    with pytest.raises(TypeError):
        type(S.x)(1, 2)
    with pytest.raises(TypeError):
        type(S.x)(1, 2, 3)
    with pytest.raises(TypeError):
        type(S.x)(1, 2, 3, 4)
    with pytest.raises(TypeError):
        type(S.x)(1, 2, 3, 4, 5)
    with pytest.raises(TypeError):
        type(S.x)(1, 2, 3, 4, 5, 6)
    with pytest.raises(TypeError):
        type(S.x)(1, 2, 3, 4, 5, 6, 7)
    with pytest.raises(TypeError):
        type(S.x)(1, 2, 3, 4, 5,
