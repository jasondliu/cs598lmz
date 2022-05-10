import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = ctypes.c_int(5)

c = C()
print type(c.x) is ctypes.CField
print c.x.__class__ is ctypes.CField
print c.x.value

c.x = ctypes.c_int(6)
print c.x.value
</code>

