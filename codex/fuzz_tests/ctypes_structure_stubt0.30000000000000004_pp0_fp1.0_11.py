import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

# ctypes.c_int.from_buffer(s, 0)
# ctypes.c_int.from_buffer(s, 4)

# ctypes.c_int.from_buffer(s, 0).value
# ctypes.c_int.from_buffer(s, 4).value

# ctypes.c_int.from_buffer(s, 0).value = 3
# ctypes.c_int.from_buffer(s, 4).value = 4

# print(s.x, s.y)

# ctypes.c_int.from_buffer(s, 0).value
# ctypes.c_int.from_buffer(s, 4).value

# ctypes.c_int.from_buffer(s, 0).value = 5
# ctypes.c_int.from_buffer(s, 4).value = 6

# print(
