import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = 1

def f():
    return C()

def g():
    return C()

def h():
    return C()

def test_getfield():
    c = f()
    assert c.x == 1
    c.x = 2
    assert c.x == 2
    assert type(c.x) is int

def test_getfield_class():
    c = g()
    assert c.x == 1
    c.x = 2
    assert c.x == 2
    assert type(c.x) is int

def test_getfield_ctypes():
    c = h()
    assert c.x == 1
    c.x = 2
    assert c.x == 2
    assert type(c.x) is int
