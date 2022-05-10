import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class E(ctypes.Structure):
    def __setattr__(self, name, value):
        self._fields_ = [('a', ctypes.c_int),
                         ('b', ctypes.c_int)]
        ctypes.Structure.__setattr__(self, name, value)

def test_type():
    assert type(S.x) is ctypes.CField
    assert S.x.type is ctypes.c_int

def test_cast():
    s = S()
    p = ctypes.cast(ctypes.byref(s), ctypes.POINTER(S.x))
    assert p.contents.value == 0
    p.contents.value = 42
    assert s.x == 42

def test_get_by_name():
    s = S()
    assert S.x.in_dll(s) == 0
    s
