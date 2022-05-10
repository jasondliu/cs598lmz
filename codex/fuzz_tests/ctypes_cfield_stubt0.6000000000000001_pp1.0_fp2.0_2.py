import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    pass

c = C()
c.x = 5

s = S()

s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s.x = c.x
s
