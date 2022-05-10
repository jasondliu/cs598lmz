import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

# Create a pointer to a structure
p = ctypes.pointer(s)

# Create a pointer to the address of the structure
p = ctypes.pointer(ctypes.pointer(s))

# Dereference the pointer to the address of the structure
print(p.contents.contents.x)

# Pointer to a pointer to a structure
p = ctypes.pointer(ctypes.pointer(s))

# Dereference the pointer to a pointer to a structure
print(p.contents.contents.x)

# Pointer to an array of structures
