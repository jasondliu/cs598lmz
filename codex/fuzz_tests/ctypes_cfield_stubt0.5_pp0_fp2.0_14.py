import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_CField_in_Structure():
    # Issue #1523
    class S(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int)]
    s = S()
    s.x = 1
    assert s.x == 1

def test_CField_in_Union():
    # Issue #1523
    class S(ctypes.Union):
        _fields_ = [('x', ctypes.c_int)]
    s = S()
    s.x = 1
    assert s.x == 1

def test_CField_in_PyCArgObject():
    # Issue #1523
    class S(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int)]
    s = S()
    a = ctypes.py_object(s)
    a.x = 1
    assert a.x == 1

def test_CField_in_PyCArrayTypeObject():
    # Issue #1523
    class S(ctypes.Structure):

