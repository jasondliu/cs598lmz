import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

# ctypes.c_int.from_address(id(s)) = 1

# ctypes.c_int.from_address(id(s) + ctypes.sizeof(ctypes.c_int)) = 2

# ctypes.c_int.from_address(id(s) + 2 * ctypes.sizeof(ctypes.c_int)) = 0

# ctypes.c_int.from_address(id(s) + 3 * ctypes.sizeof(ctypes.c_int)) = 0

# ctypes.c_int.from_address(id(s) + 4 * ctypes.sizeof(ctypes.c_int)) = 0

# ctypes.c_int.from_address(id(s) + 5 * ctypes.sizeof(ctypes.c_int)) = 0

# ctypes.c_int.from
