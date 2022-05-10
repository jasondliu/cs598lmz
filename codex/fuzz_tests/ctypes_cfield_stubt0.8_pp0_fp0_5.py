import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('spam', ctypes.c_int), ('eggs', ctypes.c_int)]

class CC(C):
    pass

class D(CC):
    pass

def test_CField_get():
    s = S()
    c = C()

    s.x = 42
    c.spam = 37
    c.eggs = 101

    # C fields are read-only
    raises(AttributeError, setattr, s.x, 'value', 23)
    raises(AttributeError, setattr, c.spam, 'value', 23)

    assert s.x == 42
    assert c.spam == 37
    assert c.eggs == 101

def test_CField_set():
    s = S()
    c = C()

    # CField is read only
    raises(AttributeError, setattr, s.x, 'value', 23)
    raises(AttributeError, setattr, c.spam, 'value', 23)

def test_CField
