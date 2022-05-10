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
# ctypes.Structure.in_dll(dll, name)
# ctypes.Structure.from_buffer(buffer)
# ctypes.Structure.from_buffer_copy(buffer)

# ctypes.Union
# ctypes.Union.from_address(address)
# ctypes.Union.in_dll(dll, name)
# ctypes.Union.from_buffer(buffer)
# ctypes.Union.from_buffer_copy(buffer)

# ctypes.BigEndianStructure
# ctypes.BigEndianStructure.from_address(address)
# ctypes.BigEndianStructure.in_dll(dll, name)
# ctypes.BigEndianStructure.from_buffer(buffer)

