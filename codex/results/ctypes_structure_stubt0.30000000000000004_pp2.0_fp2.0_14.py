import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x, s.y, s.z)

# ctypes.c_int.from_address(id(s))

print(ctypes.c_int.from_address(id(s)).value)
print(ctypes.c_int.from_address(id(s) + ctypes.sizeof(ctypes.c_int)).value)
print(ctypes.c_int.from_address(id(s) + 2 * ctypes.sizeof(ctypes.c_int)).value)
