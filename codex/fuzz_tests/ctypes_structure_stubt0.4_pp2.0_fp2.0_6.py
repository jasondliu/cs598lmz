import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()
    z = ctypes.c_int()
    def __repr__(self):
        return "S(%d,%d,%d)" % (self.x,self.y,self.z)

class T(S):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

s = S()
s.x = 1
s.y = 2
s.z = 3

t = T(10,20,30)

print s, t

# ctypes.memmove(s, t, ctypes.sizeof(S))
# ctypes.memmove(s, t, ctypes.sizeof(T))

# ctypes.memmove(s, t, ctypes.sizeof(t))

ctypes.memmove(s, t, ctypes.sizeof(t))
print s, t

# ctypes.memmove(t, s, ctypes
