import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField.__dict__

ctypes.CField.__str__(S.x)
#_______________________________________

def test_S(S):
    s = S()
    s.x = 42
    assert s.x == 42
    s.x += 1
    assert s.x == 43

test_S(S)
#_______________________________________

from ctypes import *

class S(Structure):
    _fields_ = [('x', c_int)]

#_______________________________________

from ctypes import *

class S(Structure):
    _fields_ = [('x', c_int)]

    def __init__(self, n):
        self.x = n

#_______________________________________

from ctypes import *

class S(Structure):
    _fields_ = [('x', c_int)]

    def __init__(self, n):
        self.x = n

    def __repr__(self):
        return 'S(%s)'%self.x

s = S(42)
print(s
