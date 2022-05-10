import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.CFuncPtr)]

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

def test_fields():
    # test that ctypes.Structure._fields_ is a tuple
    assert type(ctypes.Structure._fields_) is tuple
    assert type(ctypes.Structure._fields_[0]) is tuple
    assert type(ctypes.Structure._fields_[0][0]) is str
    assert type(ctypes.Structure._fields_[0][1]) is ctypes.CField
    assert type(ctypes.Structure._
