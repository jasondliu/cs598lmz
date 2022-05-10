import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    def __init__(self):
        self.x = 0

def test_get_cfield(lib, np):
    c = C()
    assert lib.PyCField_AsField(c.x) is S.x
    assert lib.PyCField_AsField(c.x) is S.x
    assert lib.PyCField_AsField(c.x) is S.x
    assert lib.PyCField_AsField(c.x) is S.x
    assert lib.PyCField_AsField(c.x) is S.x
    assert lib.PyCField_AsField(c.x) is S.x
    assert lib.PyCField_AsField(c.x) is S.x
    assert lib.PyCField_AsField(c.x) is S.x
    assert lib.PyCField_AsField(c.x) is S.x
    assert lib.PyCField_AsField(c.x) is S.x
    assert lib.PyCField_AsField(c.
