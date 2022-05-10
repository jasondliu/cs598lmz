import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    s = ctypes.c_char_p

s = S()
s.x = 1
s.y = 2
s.z = 3
s.s = "hello"

print(s.x, s.y, s.z, s.s)
</code>

