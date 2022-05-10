import ctypes

class S(ctypes.Structure):
    x = [ctypes.c_int, ctypes.c_int]

s = S()
s.x[0] = 1
s.x[1] = 2
print s.x[0], s.x[1]
print s.x[0] == s.x[1]

s2 = s
s2.x[0] = 3
print s.x[0], s.x[1]
print s.x[0] == s.x[1]

s_copy = S()
ctypes.memmove(ctypes.addressof(s_copy), ctypes.addressof(s), ctypes.sizeof(s))
print s_copy.x[0], s_copy.x[1]
print s_copy.x[0] == s_copy.x[1]

s_copy.x[0] = 4
print s.x[0], s.x[1]
print s.x[0] == s.x[1]
