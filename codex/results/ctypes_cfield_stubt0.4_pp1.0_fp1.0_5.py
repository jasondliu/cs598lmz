import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

class E(C):
    _fields_ = [('y', ctypes.c_int)]

class F(D, E):
    _fields_ = [('z', ctypes.c_int)]

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int)]

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int)]

class I(G, H):
    _fields_ = [('w', ctypes.c_int)]

def test_fields():
    assert S._fields_ == [('x', ctypes.c
