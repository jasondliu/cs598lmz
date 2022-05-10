import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.ctype = ctypes.get_ctype(ctypes.CField)
ctypes.CField.__reduce_ex__ = lambda self, proto: (type(self), ())

class T(ctypes.Structure):
    pass

t = T()
T._fields_ = [('s', S())]
v = t.s.x
