import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

def test_cfield():
    s = S()
    s.x = 42
    c = C()
    c.x = s.x
    assert c.x == 42
    d = D()
    d.x = 42
    e = E()
    e.x = d.x
    assert e.x == 42

def test_cfield_in_union():
    class S(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int)]
    class U(ctypes.Union):
        _fields_ = [('s', S)]
    u = U()
    u.s.x = 42
    assert u.s.x == 42

def test_
