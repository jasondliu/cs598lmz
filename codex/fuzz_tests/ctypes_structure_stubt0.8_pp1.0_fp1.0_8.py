import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double

e = ctypes.POINTER(S)()

e = ctypes.pointer(S())
e.contents.x = 1.0
e.contents.y = 2.0

print "e.contents.x =", e.contents.x
print "e.contents.y =", e.contents.y

print "e.contents.x =", ctypes.addressof(e.contents).contents.x
print "e.contents.y =", ctypes.addressof(e.contents).contents.y
