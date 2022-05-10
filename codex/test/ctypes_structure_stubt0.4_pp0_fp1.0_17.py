import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)

# ctypes.Structure.from_address(address)
# ctypes.Structure.in_dll(dll, name)
# ctypes.Structure.from_buffer(buffer)
# ctypes.Structure.from_buffer_copy(buffer)
# ctypes.Structure.from_param(obj)

# ctypes.Structure.__getattribute__(self, name)
# ctypes.Structure.__setattr__(self, name, value)
# ctypes.Structure.__delattr__(self, name)

# ctypes.Structure.__repr__(self)
# ctypes.Structure.__str__(self)

# ctypes.Structure.__bytes__(self)
# ctypes.Structure.__eq__(self, other)
# ctypes.Structure.__ne__(self, other)
