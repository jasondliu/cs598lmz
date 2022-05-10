import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    pass
C._fields_ = [('x', ctypes.c_int)]
c = C()
c.x

C._fields_ = [('x', ctypes.c_char_p)]
c.x

class D(ctypes.Structure):
    pass
D._fields_ = [('x', ctypes.c_char_p)]
d = D()
d.x = b'abc'

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char_p)]
e = E()
e.x = b'abc'

class F(ctypes.Structure):
    pass
f = F()
f.x = b'abc'

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char_p)]
g = G()
g.x = b'abc'

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char_
