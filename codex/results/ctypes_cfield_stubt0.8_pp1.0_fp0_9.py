import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.Structure):
    pass
A.b = ctypes.c_ubyte
A.c = ctypes.c_int
A._fields_ = [('a', ctypes.c_longlong),
              ('b', ctypes.c_ubyte),
              ('c', ctypes.c_int),
              ('d', ctypes.c_char)]

class B(ctypes.Structure):
    _fields_ = [('b', ctypes.c_ubyte),
                ('a', A)]

b = B()
b.a.a = 0x12345678
b.a.b = 0x44
b.a.c = -1
b.a.d = 'a'

# read b.a.a, which is the first field of A.
print b.b
print b.a.a

# read b.a.b, which is the second field of A
print b.a.b

# read b.a.c, which is the third field of A
print b.a.
