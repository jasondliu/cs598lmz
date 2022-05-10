import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [('i', ctypes.c_int),
                ('d', ctypes.c_double),
                ('c', ctypes.c_char)]

s = S()
print(s.i, s.d, s.c)

s.i = 5
s.d = 3.14
s.c = b'x'
print(s.i, s.d, s.c)

class D(ctypes.Structure):
    pass

D._fields_ = [('s', S), ('d1', ctypes.c_double), ('d2', ctypes.c_double)]

d = D()
print(d.s.i, d.s.d, d.s.c, d.d1, d.d2)

ctypes.addressof(d.s)
ctypes.addressof(d.d1)
ctypes.addressof(d.d2)
ctypes.addressof(d.s) == ctypes.addressof(d)
ctypes.addresso
