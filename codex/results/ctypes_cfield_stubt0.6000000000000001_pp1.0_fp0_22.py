import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self._data = ctypes.c_int(42)
    x = property(fget=lambda self: self._data)

c = C()
print repr(c.x)
print repr(c.x)
print repr(c.x)
print "c.x is", ctypes.CField
print "c.x is", type(c.x)
print

class C(object):
    def __init__(self):
        self._data = ctypes.c_int(42)
    x = property(fget=lambda self: self._data,
                 fset=lambda self, value: setattr(self, "_data", value))

c = C()
print repr(c.x)
print repr(c.x)
print repr(c.x)
print "c.x is", ctypes.CField
print "c.x is", type(c.x)
print

class C(object):
    def __init__(self):
        self._data = c
