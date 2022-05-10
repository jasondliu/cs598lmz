import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = 1

c = C()
ctypes.cast(ctypes.pointer(c), ctypes.POINTER(S)).contents.x = 2
print c.x
