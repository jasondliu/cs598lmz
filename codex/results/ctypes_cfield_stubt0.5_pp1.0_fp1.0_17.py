import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class C(object):
    def __init__(self):
        self.x = S()

c = C()
print c.x.x
c.x.x = 42
print c.x.x

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class C(object):
    def __init__(self):
        self.x = S()

c = C()
c.x.x = 42
print c.x.x

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class C(object):
    def __init__(self):
        self.x = S()

c = C()
c.x.x = 42
print c.x.x

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

