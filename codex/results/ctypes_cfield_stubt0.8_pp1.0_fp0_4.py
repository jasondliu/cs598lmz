import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    def __init__(self):
        self.x = S()
        self.x.x = 42
    def __eq__(self, other):
        return (self.x.x == other.x.x)

c = C()

def m1(x):
    x.x.x = 3

def m2(x):
    s = S()
    s.x = 44
    x.x = s

def m3(x):
    x.x = S()
    x.x.x = 44

def m4(x):
    del x.x

def m5(x):
    globals()['x'] = x
    del x.x

class T(ctypes.Structure):
    _fields_ = [('x', ctypes.c_longlong)]
    _anonymous_ = ['x']

# 'x' on a ctypes structure can't be used like this
def m6(x):
    x.x = 3

def m7(x):
    x.x
