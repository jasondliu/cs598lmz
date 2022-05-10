import ctypes

class S(ctypes.Structure):
    x = 1
    y = 2
S_ = ctypes.Structure("S_", [("x", ctypes.c_int), ("y", ctypes.c_int)])

# XXX no c_bool

print "original:"
print S
print S()
print S.x, S.y
print S().x, S().y

del S
del S_

print "after del:"
print ctypes.Structure
print ctypes.Structure("XXX", [("x", ctypes.c_int), ("y", ctypes.c_int)])

print ctypes.Structure
print ctypes.Structure("XXX", [])

print ctypes.Structure
print ctypes.Structure("XXX", [("x", ctypes.c_int)])

print ctypes.Structure
print ctypes.Structure("XXX", [("x", ctypes.c_int), ("y", ctypes.c_int)])
