import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', S)]

c = C()
c.x.x = 3

v = ctypes.c_void_p()
ctypes.pointer(v)[0] = ctypes.addressof(c)

p = ctypes.cast(v, ctypes.POINTER(C))
print p.contents.x.x
print ctypes.addressof(p.contents)
print p.contents.x.x
