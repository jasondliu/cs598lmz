import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)

s = S()
s.x = 5
s.x = 'hello'
print(s.x)
