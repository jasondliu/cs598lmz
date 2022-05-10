import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char_p)]

c = C()
c.x = 3
print(c.x)
print(C.x)
print(c.x == C.x)

d = D()
try:
    d.x = 3
except TypeError:
    print('TypeError')
