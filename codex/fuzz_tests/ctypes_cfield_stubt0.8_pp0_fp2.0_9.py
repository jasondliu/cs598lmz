import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class FieldPtr(ctype_pointer):
    _type_ = ctypes.CField

def test_cfield_address():
    f = FieldPtr()
    p = addressof(S.x)
    assert f.from_address(p) is S.x
    assert f.from_address(p)._offset_ == S.x._offset_

def test_cfield_offset():
    assert S.x._offset_ == offsetof(S, "x")
