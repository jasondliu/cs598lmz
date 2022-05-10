import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_instance():
    s = S()
    s.x = 10
    assert s.x == 10
    assert type(s.x) is int

class S2(ctypes.Structure):
    pass
S2._fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S2.x)

def test_cfield_instance2():
    s = S2()
    s.x = 10
    assert s.x == 10
    assert type(s.x) is int

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S3.x)

def test_cfield_class():
    s = S3()
    s.x = 10
    assert s.x == 10
    assert type(s.x) is int

class S4(ctypes.Structure):
    pass
S4._fields_ = [('x', ctypes.c_int)]

