import ctypes
# Test ctypes.CField
class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class T(ctypes.Structure):
    _fields_ = [("s", S),
                ("c", ctypes.c_char)]

t = T()
t.s.a = 1
t.s.b = 2
t.c = 'x'

print t.s.a, t.s.b, t.c

# Test ctypes.CField.from_address
class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class T(ctypes.Structure):
    _fields_ = [("s", S),
                ("c", ctypes.c_char)]

t = T()
t.s.a = 1
t.s.b = 2
t.c = 'x'

s = ctypes.CField.from_address(t, c
