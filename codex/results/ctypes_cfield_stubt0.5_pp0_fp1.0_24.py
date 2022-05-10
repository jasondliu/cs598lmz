import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

s = S()
c = C()
s.x = 42
c.x = 42

def test_c_int_is_int():
    assert type(s.x) is int
    assert type(c.x) is ctypes.c_int

def test_c_int_is_not_CField():
    assert type(s.x) is not ctypes.CField
    assert type(c.x) is not ctypes.CField

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

s = S()
c = C()
s.x = 42
c.x = 42

def test_c_int_is_int():
    assert type(s.x) is
