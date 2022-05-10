import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

# ctypes.c_int.from_address(id(s))
# ctypes.c_int.from_address(id(s) + ctypes.sizeof(ctypes.c_int))

print(ctypes.c_int.from_address(id(s)).value)
print(ctypes.c_int.from_address(id(s) + ctypes.sizeof(ctypes.c_int)).value)

# ctypes.c_int.from_address(id(s)).value = 3
# ctypes.c_int.from_address(id(s) + ctypes.sizeof(ctypes.c_int)).value = 4

print(s.x, s.y)

# ctypes.pointer(s)
# ctypes.pointer(s)[0]
# ctypes.pointer(s)[1]

print(ctypes
