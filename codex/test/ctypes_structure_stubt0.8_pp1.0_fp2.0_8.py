import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)
    z = ctypes.c_int(3)

s1 = S()
s2 = S()

# Accessing the attributes via the instance attribute
print(s1.x, s1.y, s1.z)

# Accessing the attributes via the fields dictionary attribute
