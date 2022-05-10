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

# ctypes.c_int is a subclass of int
print(isinstance(s.x, int))

# ctypes.c_int is not a subclass of S
print(isinstance(s.x, S))

# ctypes.c_int is not a subclass of ctypes.Structure
print(isinstance(s.x, ctypes.Structure))

# ctypes.c_int is not a subclass of ctypes.Union
print(isinstance(s.x, ctypes.Union))

# ctypes.c_int is not a subclass of ctypes.Array
print(isinstance(s.x, ctypes.Array))

# ctypes.c_int is not a subclass of ctypes.POINTER
