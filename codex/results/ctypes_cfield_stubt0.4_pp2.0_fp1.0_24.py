import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = None

def test_cfield_setattr():
    s = S()
    c = C()
    c.x = s.x
    assert type(c.x) is ctypes.CField
    c.x = 123
    assert type(c.x) is ctypes.CField
    assert s.x == 123
    assert c.x == 123

def test_cfield_getattr():
    s = S()
    c = C()
    c.x = s.x
    assert type(c.x) is ctypes.CField
    assert c.x == 0
    c.x = 123
    assert c.x == 123

def test_cfield_getattr_setattr():
    s = S()
    c = C()
    c.x = s.x
    assert type(c.x) is ctypes.CField
    assert c.x == 0
    c.x = 123
    assert c.x == 123
    c.
