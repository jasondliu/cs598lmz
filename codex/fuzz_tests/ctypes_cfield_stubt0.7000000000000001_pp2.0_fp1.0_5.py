import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = 0
        self.y = ''

c = C()

# ctypes.c_int.from_address(id(c.x))
ctypes.cast(id(c.x), ctypes.POINTER(ctypes.c_int))
