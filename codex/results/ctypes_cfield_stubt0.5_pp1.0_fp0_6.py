import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert isinstance(S.x, ctypes.CField)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self):
        self.x = 42

def test_cfield_init():
    s = S()
    assert isinstance(s.x, ctypes.c_int)
    assert s.x == 42

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self):
        self.x = 42

def test_cfield_init_overwrite():
    s = S()
    s.x = 43
    assert isinstance(s.x, ctypes.c_int)
    assert s.x == 43

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self):
        self.x = 42

def test_cfield
