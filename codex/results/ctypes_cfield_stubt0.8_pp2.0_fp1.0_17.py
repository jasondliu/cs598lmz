import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    __slots__ = ['x']

def make_C():
    c = C()
    c.x = 42
    return c

def make_S():
    s = S()
    s.x = 42
    return s

def pickle_test():
    import pickle
    c1 = make_C()
    s1 = make_S()
    c2 = pickle.loads(pickle.dumps(c1, -1))
    s2 = pickle.loads(pickle.dumps(s1, -1))
    assert c1.x == c2.x
    assert s1.x == s2.x
    assert type(c1.x) is int
    assert type(c2.x) is int
    assert type(s1.x) is ctypes.CField
    assert type(s2.x) is ctypes.CField

def copy_test():
    import copy
    c1 = make_C()
    s1 = make_S()
    c2 = copy
