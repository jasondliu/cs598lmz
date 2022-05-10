import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField), ('y', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CField), ('y', ctypes.c_int)]

s = S()
c = C()
d = D()

print s.x
print c.x
print d.x

s.x = 1
c.x = 2
d.x = 3

print s.x
print c.x
print d.x

print S.x
print C.x
print D.x

print type(S.x)
print type(C.x)
print type(D.x)

print type(s.x)
print type(c.x)
print type(d.x)

print type(s)
print type(c)
print type(d)

print ctypes.CField
print ctypes.CField.__bases__

print ctypes.c_int
