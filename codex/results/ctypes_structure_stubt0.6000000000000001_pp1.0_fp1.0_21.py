import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()

s.x = 1
s.y = 2
s.z = 3

print s.x, s.y, s.z

print
print "sizeof(s) = %d" % ctypes.sizeof(s)
print "s.x = %d" % s.x
print "s.y = %d" % s.y
print "s.z = %d" % s.z

print "s.x = %d" % s.x
print "s.y = %d" % s.y
print "s.z = %d" % s.z

print "&s = %x" % ctypes.addressof(s)
print "&s.x = %x" % ctypes.addressof(s.x)
print "&s.y = %x" % ctypes.addressof(s.y)
print "&s.z = %x" % ctypes.
