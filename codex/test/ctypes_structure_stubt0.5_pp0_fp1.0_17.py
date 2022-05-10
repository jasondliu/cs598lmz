import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

    def __repr__(self):
        return 'S(%s, %s)' % (self.x, self.y)

s = S()
s.x = 1
s.y = 2
print(s)

s2 = s
s2.x = 3
print(s)
