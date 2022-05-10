import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

class D(C):
    _fields_ = [('z', ctypes.c_int)]

class E(D):
    _fields_ = [('t', ctypes.c_int)]

class F(ctypes.Structure):
    pass
F._fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

class G(F):
    pass
G._fields_ = [('z', ctypes.c_int), ('t', ctypes.c_int)]

def test_fields():
    assert C._fields_ == [('x', ctypes.c_int), ('y', ctypes.c_int)]
    assert D._fields_ == [('x', ctypes.c_int), ('y', ctypes.c_int),
                          ('z', ctypes.c_int)]
    assert E._fields_ == [('x', c
