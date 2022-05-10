import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)

s = S()
print s.x
print s.y

ctypes.c_int.__getitem__(s, 0)
ctypes.c_int.__setitem__(s, 0, 3)
print s.x
print s.y

ctypes.c_int.__getitem__(s, 1)
ctypes.c_int.__setitem__(s, 1, 4)
print s.x
print s.y

print ctypes.c_int.__getitem__(s, 2)
ctypes.c_int.__setitem__(s, 2, 5)
print s.x
print s.y

try:
    ctypes.c_int.__getitem__(s, 3)
except IndexError:
    print "IndexError"

try:
    ctypes.c_int.__setitem__(s, 3, 5)
except IndexError:
    print "IndexError"

print s.
