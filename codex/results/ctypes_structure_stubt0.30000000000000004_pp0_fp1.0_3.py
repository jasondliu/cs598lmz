import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2
print(s.x, s.y)

# ctypes.c_int(1)
# ctypes.c_int(2)

# s.x = ctypes.c_int(1)
# s.y = ctypes.c_int(2)

# print(s.x, s.y)

# s.x = 1
# s.y = 2

# print(s.x, s.y)

# s.x = ctypes.c_int(1)
# s.y = ctypes.c_int(2)

# print(s.x, s.y)

# s.x = ctypes.c_int(1)
# s.y = ctypes.c_int(2)

# print(s.x, s.y)

# s.x = ctypes.c_int(1)
# s.y = ctypes.c_
