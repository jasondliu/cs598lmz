import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_var(F):

    class S(ctypes.Structure):
        _fields_ = [('x', F)]

    s = S(42)
    assert s.x == 42
    s.x += 1
    assert s.x == 43

def test_byref(F):

    class S(ctypes.Structure):
        _fields_ = [('x', F)]

    s = S(42)
    i = ctypes.c_int(0)
    ctypes.pointer(s).contents.__setattr__('x', ctypes.byref(i))
    assert i.value == 42

def test_ptr(F):

    class S(ctypes.Structure):
        _fields_ = [('x', F)]

    s = S(42)
    i = ctypes.c_int(0)
    ctypes.pointer(s).contents.__setattr__('x', ctypes.pointer(i))
    assert i.value == 42

def test_pointer(F):
    class S(ctypes
