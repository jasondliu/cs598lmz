import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class T(object):
    def __init__(self):
        self._wrapper_cache = {'x': 42}

s = S()
s.x = 42
t = T()
s.x = t.x
s.x = 42
s.x = t.x
