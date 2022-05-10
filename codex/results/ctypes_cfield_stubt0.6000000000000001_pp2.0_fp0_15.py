import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test(S):
    s = S()
    print(S.x)
    print(type(S.x))
    print(S.x.offset)
    print(S.x.size)
    print(s.x)
    print(type(s.x))
    print(s.x.offset)
    print(s.x.size)

test(S)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self):
        self.x = 42

test(S)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self):
        self.x = -42

test(S)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self):
        self.x = 0x7fffffff

test(S)

class S(
