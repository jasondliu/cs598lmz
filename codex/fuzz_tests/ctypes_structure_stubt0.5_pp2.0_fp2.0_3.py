import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()
    y = ctypes.c_long()

s = S()
s.x = 1
s.y = 2

# test __getattr__
print s.x, s.y

# test __setattr__
s.x = 3
s.y = 4
print s.x, s.y

# test __delattr__
del s.x
del s.y
try:
    print s.x, s.y
except AttributeError:
    print "OK"
