import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('s', S), ('a', ctypes.c_int)]

c = C()
c.s.x = 1

print repr(C.s.offset)
print repr(C.s.size)
print repr(C.s.index)
print repr(C.a.index)
print repr(C.s.index + C.s.x.offset)
print repr(C.s.index + C.s.x.offset + C.s.x.size)
print repr(C.s.index + C.s.x.offset + C.s.x.size + C.a.size)

print
print repr(c.s.x)
print repr(ctypes.cast(c.s.x, ctypes.c_void_p).value)
print repr(c.a)
print repr(ctypes.cast(c.a, ctypes.c_void_p).value)

assert C.s.index + C.s.x.offset == ctypes.
