import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 2
    y = ctypes.c_char * 2
    z = ctypes.c_char * 2

s = S()

s.x = 'a'
s.y = 'b'
s.z = 'c'

print(s.x)
print(s.y)
print(s.z)

print(ctypes.sizeof(s))
