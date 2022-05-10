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

# ctypes.Structure.from_address(address)
# ctypes.Structure.from_buffer(buffer)
# ctypes.Structure.from_buffer_copy(buffer)

# ctypes.Union

class U(ctypes.Union):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ('z', ctypes.c_int),
    ]

u = U()

u.x = 1
u.y = 2
u.z = 3

print(u.x, u.y, u.z)

# ctypes.Union.from_address(address)
# ctypes.Union.from_buffer(buffer)
# ctypes.Union.from_buffer_copy
