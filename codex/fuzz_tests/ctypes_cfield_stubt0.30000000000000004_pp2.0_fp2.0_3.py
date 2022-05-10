import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

class E(D):
    _fields_ = [('z', ctypes.c_int)]

def test_field_offset():
    assert S.x.offset == 0
    assert C.x.offset == 0
    assert D.x.offset == 0
    assert D.y.offset == 4
    assert E.x.offset == 0
    assert E.y.offset == 4
    assert E.z.offset == 8

def test_field_size():
    assert S.x.size == 4
    assert C.x.size == 4
    assert D.x.size == 4
    assert D.y.size == 4
    assert E.x.size == 4
    assert E.y.size == 4
    assert E.z.size == 4

def test_field_name():
    assert S.x.name == 'x'
