import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

def test_CField():
    assert isinstance(C.x, ctypes.CField)
    assert isinstance(D.x, ctypes.CField)
    assert isinstance(D.y, ctypes.CField)

def test_CField_name():
    assert C.x.name == 'x'
    assert D.x.name == 'x'
    assert D.y.name == 'y'

def test_CField_offset():
    assert C.x.offset == 0
    assert D.x.offset == 0
    assert D.y.offset == ctypes.sizeof(ctypes.c_int)

def test_CField_size():
    assert C.x.size == ctypes.sizeof(ctypes.c_int)
    assert D.x.size == ctypes.sizeof(ctypes
