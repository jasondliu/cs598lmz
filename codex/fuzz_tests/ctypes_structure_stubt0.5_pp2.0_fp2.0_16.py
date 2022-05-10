import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()


s = S()
s.x = 3
print(s.x)

s1 = S()
s1.x = 4
print(s1.x)

s1.x = s.x
print(s1.x)

s.x = 5
print(s1.x)
