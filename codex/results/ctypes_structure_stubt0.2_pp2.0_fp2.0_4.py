import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

# ctypes.Structure is a subclass of ctypes.Union

class U(ctypes.Union):
    x = ctypes.c_int
    y = ctypes.c_int

u = U()
u.x = 1
u.y = 2

print(u.x, u.y)

# ctypes.Union is a subclass of ctypes.BigEndianStructure

class B(ctypes.BigEndianStructure):
    x = ctypes.c_int
    y = ctypes.c_int

b = B()
b.x = 1
b.y = 2

print(b.x, b.y)

# ctypes.BigEndianStructure is a subclass of ctypes.LittleEndianStructure

class L(ctypes.LittleEndianStructure):
    x = ctypes.c_int
    y
