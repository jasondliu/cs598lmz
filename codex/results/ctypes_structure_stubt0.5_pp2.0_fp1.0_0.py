import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print s.x, s.y

a = ctypes.addressof(s)
print a

b = ctypes.byref(s)
print b

c = ctypes.pointer(s)
print c

print c.contents.x
print c.contents.y

d = ctypes.cast(a, ctypes.POINTER(S))
print d

print d.contents.x
print d.contents.y

e = ctypes.cast(a, ctypes.POINTER(ctypes.c_int))
print e

print e.contents

f = ctypes.cast(a, ctypes.POINTER(ctypes.c_int))
print f

print f[0]
print f[1]

g = ctypes.cast(a, ctypes.POINTER(ctypes.c_int * 2))
print g

print g.contents
