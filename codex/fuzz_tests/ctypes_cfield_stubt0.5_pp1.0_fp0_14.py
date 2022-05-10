import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s = S()
s.x = 1
s.y = 2

s.x = s.y

s.x = 1
s.y = 2

s.x = s.y

# this is a comment

s.x = 1
s.y = 2

s.x = s.y

def f():
    class S(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

    s = S()
    s.x = 1
    s.y = 2

    s.x = s.y

f()

def g():
    class S(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

    s = S()
    s.x = 1
    s.y = 2
