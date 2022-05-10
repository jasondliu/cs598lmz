import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int * 2

def f(): return 1, [1]

s = S()
s.x[0], s.x[1] = f()
print "s.x contains", repr(s.x[:])
print "S.x is", repr(S.x)
