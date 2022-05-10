import ctypes

class S(ctypes.Structure):
    x = ctypes.c_size_t
    y = ctypes.c_size_t

s = S()
s.x = 1
s.y = 2

print(ctypes.sizeof(s))
print(s.x)
print(s.y)

# <ref>
