import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

# ctypes.c_int.from_address(id(s))

# print(ctypes.c_int.from_address(id(s)))

# print(ctypes.c_int.from_address(id(s)).value)

# print(ctypes.c_int.from_address(id(s)).value)

# print(ctypes.c_int.from_address(id(s)).value)

# print(ctypes.c_int.from_address(id(s)).value)

# print(ctypes.c_int.from_address(id(s)).value)

# print(ctypes.c_int.from_address(id(s)).value)

# print(ctypes.c_int.from_address(id(s)).value)

# print(ctypes.c_int.from_address(id
