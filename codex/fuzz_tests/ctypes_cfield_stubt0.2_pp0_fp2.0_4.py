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

def test_from_address():
    s = S()
    p = ctypes.pointer(s)
    assert ctypes.CField.from_address(p, S, 'x') is s.x
    assert ctypes.CField.from_address(p, D, 'x') is s.x
    assert ctypes.CField.from_address(p, E, 'x') is s.x
    raises(TypeError, ctypes.CField.from_address, p, S, 'y')
    raises(TypeError, ctypes.CField.from_address, p, D, 'y')
    raises(TypeError, ctypes.CField.from_address, p, E, 'y')
    raises(TypeError, ctypes
