import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)

s = S()

# This is a bug:
# The address of s.x is computed as a global variable,
# but it is not a global variable, it is a member of s.
print(ctypes.addressof(s.x))

# This is correct:
print(ctypes.addressof(s) + ctypes.sizeof(ctypes.c_int))
