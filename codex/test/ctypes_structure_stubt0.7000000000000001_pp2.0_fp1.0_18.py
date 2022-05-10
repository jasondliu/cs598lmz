import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p
    y = ctypes.c_int

s = S()
s.x = "hello"
s.y = 4
s.x = "world"

print(s.x)
print(s.y)
