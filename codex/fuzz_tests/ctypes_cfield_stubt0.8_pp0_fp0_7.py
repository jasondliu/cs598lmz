import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(object):
    pass
S.x.__dict__['__repr__'](S.x).__class__ = type
X.__repr__ = S.x.__dict__['__repr__']
print X() # '<X object at 0x...>'
