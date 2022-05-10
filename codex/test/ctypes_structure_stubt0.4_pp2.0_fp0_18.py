import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p

s = S()
s.x = "hello"
s.x = "world"
print(s.x)
