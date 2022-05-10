import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_longlong
    z = ctypes.c_float

class T(ctypes.Structure):
    w = ctypes.c_short

class U(ctypes.Union):
    _fields_ = [('s', S),
                ('t', T)]

class V(ctypes.Structure):
    _fields_ = [('u', U)]


def test_field_access():
    v = V()
    v.u.s.x = 10.25
    assert v.u.s.x == 10.25

def test_substruct_access():
    v = V()
    v.u.s.x = 10.25
    v.u.s.y = 42
    v.u.s.z = -13.5
    assert v.u.s.x == 10.25
    assert v.u.s.y == 42
    assert v.u.s.z == -13.5

def test_subunion_access():
    v = V()
   
