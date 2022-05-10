import ctypes
# Test ctypes.CField
class S(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [('s', S),
                ('c', ctypes.c_char)]

c = C()
c.s.a = 123
print(c.s.a, c.s.b)

# Test ctypes.CField
class S(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [('s', S),
                ('c', ctypes.c_char)]

c = C()
c.s.a = 123
print(c.s.a, c.s.b)

# Test ctypes.CField
class S(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b',
