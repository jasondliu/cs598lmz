import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CField),
                ('y', ctypes.CField)]

c = C()
d = D()

# This test is not very interesting, but it should not crash.
c.x = d.x
