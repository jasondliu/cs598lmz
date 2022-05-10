import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint16(1)
    y = ctypes.c_uint16(2)

s = S()

# This is the line that breaks everything
s.x = ctypes.c_uint16(2)

print(s.x)
print(s.y)
