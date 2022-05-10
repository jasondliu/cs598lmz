import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __getattribute__(self, name):
        return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if isinstance(value, ctypes.CField):
            value = value.value
        object.__setattr__(self, name, value)

class D(C):
    pass

class E(C):
    _fields_ = [('x', ctypes.c_int)]

def test(C):
    s = S()
    s.x = 42
    c = C()
    c.x = s.x
    s.x = 43
    assert c.x == 42

test(C)
test(D)
test(E)

print 'OK'
