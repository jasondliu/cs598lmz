import ctypes
# Test ctypes.CField

class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class T(ctypes.Structure):
    _fields_ = [("s", S),
                ("c", ctypes.c_char)]

s = S()
s.a = 1
s.b = 2

t = T()
t.s = s
t.c = 'x'

print t.s.a, t.s.b, t.c

t.s.a = 3
t.s.b = 4
t.c = 'y'

print t.s.a, t.s.b, t.c

print S.a.offset, S.b.offset, T.s.offset, T.c.offset

print S.a.size, S.b.size, T.s.size, T.c.size

print S.a.__doc__

print S.a.__dict__

print S.a.__get__
