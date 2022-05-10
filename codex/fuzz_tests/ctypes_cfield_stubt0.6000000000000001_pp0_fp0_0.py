import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_fields():
    class S(ctypes.Structure):
        _fields_ = [('a', ctypes.c_int),
                    ('b', ctypes.c_int)]
    self = S()
    assert isinstance(self._fields_[0], ctypes.CField)
    self.a = 1
    assert self.a == 1
    self.b = 2
    assert self.b == 2
    self.a = 3
    assert self.a == 3
    assert self.b == 2

def test_subclasses():
    class S(ctypes.Structure):
        _fields_ = [('a', ctypes.c_int),
                    ('b', ctypes.c_int)]
    class T(S):
        _fields_ = [('c', ctypes.c_int)]
    self = T()
    assert isinstance(self._fields_[0], ctypes.CField)
    self.a = 1
    assert self.a == 1
    self.b = 2
    assert self.b == 2
    self
