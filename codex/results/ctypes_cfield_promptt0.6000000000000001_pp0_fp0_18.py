import ctypes
# Test ctypes.CField.

class S(ctypes.Structure):
    _fields_ = [("foo", ctypes.c_int, 1),
                ("bar", ctypes.c_int, 1)]

class U(ctypes.Union):
    _fields_ = [("foo", ctypes.c_int, 1),
                ("bar", ctypes.c_int, 1)]

s = S()
u = U()

print "before", s.foo, s.bar
s.foo = 1
print "after", s.foo, s.bar

print "before", u.foo, u.bar
u.foo = 1
print "after", u.foo, u.bar
