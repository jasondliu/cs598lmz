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

# ctypes.c_int is a class, not an instance
print(type(ctypes.c_int))

# ctypes.c_int() is an instance
print(type(ctypes.c_int()))

# ctypes.c_int() is an instance of ctypes.c_int
print(isinstance(ctypes.c_int(), ctypes.c_int))

# ctypes.c_int is a class, not an instance
print(isinstance(ctypes.c_int, ctypes.c_int))

# ctypes.c_int is a class, not an instance
print(isinstance(ctypes.c_int, type))

# ctypes.c_int() is an instance
print(isinstance(ctypes.c_int(), type))
