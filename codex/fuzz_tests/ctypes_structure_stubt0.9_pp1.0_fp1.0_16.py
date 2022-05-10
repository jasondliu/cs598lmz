import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()

s = S()
s.x

s.x = 23.45
s.x

S.x
S.x.__doc__
S.x.__get__
S.x.__set__
S.x.__delete__
S.x.__getitem__
S.x.__setitem__

S.x.__doc__    = "aaaaargh"
S.x.__doc__
del S.x.__doc__

s = S()
s.x

s.x = 23.45
s.x

s.x += 33.33
s.x

class S_(ctypes.Structure):
    _fields_ = [("x",  ctypes.c_double)]
s = S_()
s.x
s.x = 23.45
s.x


class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    def __init__(self, a):
        ctypes.Structure.__init__
