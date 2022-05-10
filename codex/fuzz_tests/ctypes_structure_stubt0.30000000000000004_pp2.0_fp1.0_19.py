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

# ctypes.Structure.in_dll(dll, name)
#   Return a ctypes instance of the structure, initialized with the data in the global variable name in the specified dll.

# ctypes.Structure.from_address(address)
#   Return a ctypes instance of the structure, initialized with the data in the memory block pointed to by address.

# ctypes.Structure.from_buffer(buffer)
#   Return a ctypes instance of the structure, initialized with the data in the buffer.

# ctypes.Structure.from_buffer_copy(buffer)
#   Return a ctypes instance of the structure, initialized with the data in the buffer. The buffer is not modified.

# ctypes.Structure.from_file(file)
#   Return a ctypes instance of the structure,
