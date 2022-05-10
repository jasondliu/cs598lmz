import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_c_field_type():
    # Issue #15593
    assert type(S.x) is ctypes.CField

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

def test_c_field_type_after_subclassing():
    # Issue #15593
    assert type(S.x) is ctypes.CField

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

def test_c_field_type_after_subclassing_and_instantiation():
    # Issue #15593
    assert type(S.x) is ctypes.CField
    s = S()
    assert type(S.x) is ctypes.CField
