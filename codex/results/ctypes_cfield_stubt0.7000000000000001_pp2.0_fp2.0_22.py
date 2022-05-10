import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = 5
        self.y = 6
    def __repr__(self):
        return "<C %r %r>" % (self.x, self.y)

ctypes.CField.__get__(C().x, C, C)
ctypes.CField.__set__(C().x, C, C, 1)
ctypes.CField.__delete__(C().x, C, C)

try: ctypes.CField.__get__(C().y, C, C)
except AttributeError: pass
else: raise AssertionError

try: ctypes.CField.__set__(C().y, C, C, 1)
except AttributeError: pass
else: raise AssertionError

try: ctypes.CField.__delete__(C().y, C, C)
except AttributeError: pass
else: raise AssertionError

ctypes.POINTER(ctypes.CField)
ctypes.POINTER(ct
