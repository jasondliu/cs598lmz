import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

s = S()
print(s.x)
s.x = 1
print(s.x)

s.x = 'abc'
print(s.x)
