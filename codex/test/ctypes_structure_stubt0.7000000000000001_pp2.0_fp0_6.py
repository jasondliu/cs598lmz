import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short

s = S()
print(s.x)
s.x = 2
print(s.x)

s.x = -5
print(s.x)
s.x = 2**15-1
print(s.x)
s.x = -2**15
print(s.x)
